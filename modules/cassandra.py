import os
import time
from time import sleep
from typing import List

import cassandra
from cassandra.cluster import Cluster

import const
import db_const
from modules.database_container import DatabaseContainer
from modules.helpers import CassandraHelpers


class Cassandra(DatabaseContainer):
    # TODO: limit memory usage
    mem_limit = "4g"
    master_container = None
    session = None

    def __init__(self):
        super().__init__()

    def add_container(self) -> None:
        index = len(self.containers) + 1
        container_name = f"cassandra-{index}"
        host_port = str(9042 + index - 1)
        container_image = "cassandra:4.0"

        print(f"Cassandra #{index} is starting...")

        if index == 1:
            container = self.client.containers.run(
                name=container_name,
                image=container_image,
                ports={9042: host_port},
                privileged=True,
                detach=True,
            )
        else:
            seeds = ','.join([ip_address for ip_address in self.containers.keys()])
            container = self.client.containers.run(
                name=container_name,
                image=container_image,
                ports={9042: host_port},
                privileged=True,
                detach=True,
                environment=[f"CASSANDRA_SEEDS={seeds}"],
            )

        container_ip = self.get_fresh_attrs(container)['NetworkSettings']['IPAddress']
        self.containers[container_ip] = container
        print(f"Cassandra {container.id} started on IP {container_ip}.")
        if self.master_container is None:
            self.master_container = container
            print(f"Master Cassandra container is {container_ip}.")

        print("Waiting until connection is established", end="")
        while not self._is_connection_established():
            print(".", end="")
            sleep(1)
        print()
        print("Connection established.")

    def stop_container(self, container) -> None:
        container.stop()
        print(f"Cassandra {container.id} stopped.")

    def stop_all_containers(self) -> None:
        for container in self.containers.values():
            self.stop_container(container)
        self.containers.clear()

    def execute_query(self, sql, stdout=True) -> int:
        cmd = f"cqlsh -e {sql}"
        exit_code, output = self.master_container.exec_run(cmd, privileged=True)
        if stdout:
            if exit_code != 0:
                msg = "[Error]"
            else:
                msg = "[Success]"
            print(f"\t{output.decode('utf-8')}")
            print(f"{msg} Command '{cmd}' returned code {exit_code}.")

        return exit_code

    def _is_connection_established(self) -> bool:
        sql = "help"
        exit_code = self.execute_query(sql, stdout=False)
        if exit_code == 0:
            return True
        return False

    def initialize_database(self, stdout=False) -> List:
        self.execute_query(
            sql="\"create keyspace f1_data with replication = {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1'};\"",
            stdout=False)
        cluster = Cluster([self.get_fresh_attrs(self.master_container)['NetworkSettings']['IPAddress']])
        self.session = cluster.connect(const.CASSANDRA_KEYSPACE)
        sql_files = CassandraHelpers.get_list_of_script_files()
        results = []
        start_time = time.perf_counter()
        for file in sql_files:
            if stdout:
                print(f"Running queries from file {file}...")
            sql_file = open(os.path.join(const.CASSANDRA_SCRIPTS_FILE_DIR, file), encoding="utf-8")
            sql_as_list = sql_file.read().replace("&amp;", "").split(";")
            try:
                for line in sql_as_list:
                    to_execute = line.strip()
                    if to_execute and to_execute != ";":
                        to_execute += ";"
                        if stdout:
                            print(to_execute)
                        self.session.execute(to_execute)
            except cassandra.DriverException as e:
                print(f"Error: {e}")

            if stdout:
                print(f"Table from file {file} added.")
        elapsed_time = time.perf_counter() - start_time
        results.append(("INSERT", "-", elapsed_time))
        return results

    def select_all_data_from_columns(self, stdout=False) -> List:
        """Select All Data from Columns By Column Name"""
        results = []
        for key, value in db_const.TABLES_NAMES.items():
            if key == "JOINED":
                continue
            start_time = time.perf_counter()
            query = f'SELECT * from {value}'
            self.session.execute(query)
            elapsed_time = time.perf_counter() - start_time
            if stdout:
                print(f"time to select all rows from column {key}: {elapsed_time}s")
            results.append(("SELECT ALL DATA FROM COLUMNS", key, elapsed_time))
        return results

    def select_races_data(self, stdout=False) -> List:
        """Select All Data from Races Table"""
        start_time = time.perf_counter()
        query = f'SELECT * from {db_const.TABLES_NAMES["JOINED"]}'

        self.session.execute(query)
        elapsed_time = time.perf_counter() - start_time
        if stdout:
            print(f"All data from {db_const.TABLES_NAMES['RESULTS']} with related columns, time: {elapsed_time}s")
        return ["SELECT RACES DATA", "-", elapsed_time]

    def select_longest_lap(self, stdout=False) -> List:
        """Select Longest Lap from laptimes table"""
        start_time = time.perf_counter()
        query = f'SELECT MAX({db_const.LAPTIMES_COLUMNS["MILLISECONDS"]}) from {db_const.TABLES_NAMES["LAPTIMES"]}'
        result = self.session.execute(query).one()
        if not result:
            raise ValueError(f"Query {query} did not return anything")
        max_milliseconds = self.session.execute(query).one()[0]
        query = f'SELECT * FROM {db_const.TABLES_NAMES["LAPTIMES"]} WHERE milliseconds = {max_milliseconds} ALLOW FILTERING'
        self.session.execute(query)
        elapsed_time = time.perf_counter() - start_time
        if stdout:
            print(f"Select longest lap time, time: {elapsed_time}s")
        return ["SELECT LONGEST LAP", "-", elapsed_time]

    def select_driver_with_most_1st_positions(self, stdout=False) -> List:
        """Select Driver with the most 1st positions"""
        start_time = time.perf_counter()
        query = f'SELECT "driverId" FROM {db_const.TABLES_NAMES["QUALIFYING"]} WHERE position = 1 GROUP BY "driverId" ALLOW FILTERING'
        result = self.session.execute(query).all()
        driverId_list = ",".join([str(driverId[0]) for driverId in result]).strip(",")
        query = f'SELECT * FROM {db_const.TABLES_NAMES["DRIVERS"]} WHERE "driverId" in ({driverId_list})'
        self.session.execute(query)
        elapsed_time = time.perf_counter() - start_time
        if stdout:
            print(f"Select driver with most 1st positions, time: {elapsed_time}s")
        return ["SELECT DRIVER WITH MOST 1st POSITIONS", "-", elapsed_time]
