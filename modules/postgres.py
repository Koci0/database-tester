import os
import time
from time import sleep
from typing import List

import psycopg2
from psycopg2 import OperationalError

import const
import db_const
from modules.database_container import DatabaseContainer
from modules.helpers import PostgresHelpers


class Postgres(DatabaseContainer):
    master_container = None
    db_connection = None
    db_cursor = None

    def __init__(self):
        super().__init__()

    def add_container(self) -> None:
        index = len(self.containers) + 1
        container_name = f"postgres-{index}"
        host_port = const.POSTGRES_PORT
        container_image = "postgres:14.2"

        print(f"Postgres #{index} is starting...")

        container = self.client.containers.run(
            name=container_name,
            image=container_image,
            ports={5432: host_port},
            privileged=True,
            detach=True,
            environment=[f"POSTGRES_USER={const.POSTGRES_USER}", f"POSTGRES_PASSWORD={const.POSTGRES_PASSWORD}"]
        )

        container_ip = self.get_fresh_attrs(container)['NetworkSettings']['IPAddress']
        self.containers[container_ip] = container
        print(f"Postgres {container.id} started on IP {container_ip}.")
        self.master_container = container

        print("Waiting until connection is established", end="")
        while not self._is_connection_established():
            print(".", end="")
            sleep(1)
        print()
        print("Connection established.")

    def stop_container(self, container) -> None:
        container.stop()
        print(f"Postgres {container.id} stopped.")

    def stop_all_containers(self) -> None:
        for container in self.containers.values():
            self.stop_container(container)
        self.containers.clear()

    def execute_query(self, sql, stdout=True) -> int:
        cmd = f"psql -c {sql}"
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
        sql = r"\\help"
        exit_code = self.execute_query(sql, stdout=False)
        if exit_code == 0:
            return True
        return False

    def initialize_database(self, stdout=False) -> List:
        results = []
        self.db_connection = PostgresHelpers.get_connection_to_database()
        self.db_cursor = PostgresHelpers.get_db_cursor(self.db_connection)
        sql_files = PostgresHelpers.get_list_of_script_files()
        start_time = time.perf_counter()
        for file in sql_files:
            if stdout:
                print(f"Running queries from file {file}...")
            sql_file = open(os.path.join(const.POSTGRES_SCRIPTS_FILE_DIR, file), encoding="utf-8")
            sql_as_string = sql_file.read()
            try:
                self.db_cursor.execute(sql_as_string)
            except OperationalError as msg:
                print(f"Command skipped: {msg}")
            except psycopg2.DatabaseError as msg:
                print(f"Table exists: {msg}")
            self.db_connection.commit()
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
            self.db_cursor.execute(query)
            elapsed_time = time.perf_counter() - start_time
            if stdout:
                print(f"time to select all rows from column {key}: {elapsed_time}s")
            results.append(("SELECT ALL DATA FROM COLUMNS", key, elapsed_time))
        return results

    def select_races_data(self, stdout=False) -> List:
        """Select All Data from Results Table"""
        start_time = time.perf_counter()
        query = f'SELECT * from {db_const.TABLES_NAMES["RESULTS"]}' \
                f' inner join {db_const.TABLES_NAMES["RACES"]} r on r."{db_const.RACES_COLUMNS["RACE_ID"]}" = {db_const.TABLES_NAMES["RESULTS"]}."{db_const.RESULTS_COLUMNS["RACE_ID"]}"' \
                f' inner join {db_const.TABLES_NAMES["DRIVERS"]} d on d."{db_const.DRIVER_COLUMNS["DRIVER_ID"]}" = {db_const.TABLES_NAMES["RESULTS"]}."{db_const.RESULTS_COLUMNS["DRIVER_ID"]}"' \
                f' inner join {db_const.TABLES_NAMES["CONSTRUCTORS"]} c on c."{db_const.CONSTRUCTORS_COLUMNS["CONSTRUCTOR_ID"]}" = {db_const.TABLES_NAMES["RESULTS"]}."{db_const.RESULTS_COLUMNS["CONSTRUCTOR_ID"]}"' \
                f' inner join {db_const.TABLES_NAMES["STATUS"]} s on s."{db_const.STATUS_COLUMNS["STATUS_ID"]}" = {db_const.TABLES_NAMES["RESULTS"]}."{db_const.RESULTS_COLUMNS["STATUS_ID"]}"'

        self.db_cursor.execute(query)
        result = list(self.db_cursor.fetchall())
        elapsed_time = time.perf_counter() - start_time
        if stdout:
            print(f"All data from {db_const.TABLES_NAMES['RESULTS']} with related columns, time: {elapsed_time}s")
        return ["SELECT RSULTS DATA", "-", elapsed_time]

    def select_longest_lap(self, stdout=False) -> List:
        """Select Longest Lap from laptimes table"""
        start_time = time.perf_counter()
        query = f'SELECT * from {db_const.TABLES_NAMES["LAPTIMES"]}' \
                f' WHERE {db_const.LAPTIMES_COLUMNS["MILLISECONDS"]} = ' \
                f'(SELECT MAX({db_const.LAPTIMES_COLUMNS["MILLISECONDS"]}) FROM {db_const.TABLES_NAMES["LAPTIMES"]})'
        self.db_cursor.execute(query)
        elapsed_time = time.perf_counter() - start_time
        if stdout:
            print(f"Select longest lap time, time: {elapsed_time}s")
        return ["SELECT LONGEST LAP", "-", elapsed_time]

    def select_driver_with_most_1st_positions(self, stdout=False) -> List:
        """Select Driver with the most 1st positions"""
        start_time = time.perf_counter()
        query = f'SELECT * FROM {db_const.TABLES_NAMES["DRIVERS"]} where ' \
                f'"{db_const.DRIVER_COLUMNS["DRIVER_ID"]}" = (SELECT "{db_const.DRIVER_COLUMNS["DRIVER_ID"]}" as driver FROM (SELECT ' \
                f'"{db_const.DRIVER_COLUMNS["DRIVER_ID"]}", count( *) cnt, rank() over(ORDER BY count(*) DESC) FROM {db_const.TABLES_NAMES["QUALIFYING"]} ' \
                f'WHERE {db_const.QUALIFYING_COLUMNS["POSITION"]} = 1 GROUP BY "{db_const.DRIVER_COLUMNS["DRIVER_ID"]}") a ' \
                f'WHERE rank = 1)'
        self.db_cursor.execute(query)
        elapsed_time = time.perf_counter() - start_time
        if stdout:
            print(f"Select driver with most 1st positions, time: {elapsed_time}s")
        return ["SELECT DRIVER WITH MOST 1st POSITIONS", "-", elapsed_time]

    def remove_results(self, stdout=False) -> List:
        """Remove Results of Drivers that got position lower than 30 more than 10 times ~7k rows affected"""
        start_time = time.perf_counter()
        query = 'DELETE FROM results where "driverId" IN ' \
                '(SELECT "driverId" as driver FROM ' \
                '(SELECT DISTINCT "driverId" FROM qualifying WHERE position < 30 GROUP BY "driverId" having count(*) > 5 ) ' \
                'as newTab)'
        self.db_cursor.execute(query)
        self.db_connection.commit()
        elapsed_time = time.perf_counter() - start_time
        if stdout:
            print(f"Removing results, time: {elapsed_time}s")
        return ["REMOVE RESULTS FOR SPECIFIC DRIVERS", "-", elapsed_time]

    def update_laptimes(self, stdout=False) -> List:
        """Update lap times for races where drivers where disqualified """
        start_time = time.perf_counter()
        query = "UPDATE laptimes SET position=100, milliseconds = (milliseconds + 10000000), time= '" + "updated time" + \
                "' WHERE 'driverId' IN (SELECT 'driverId' as driver FROM " \
                "(SELECT 'driverId' FROM RESULTS WHERE position is Null OR 'positionText' = 'R') as NewTab) " \
                "OR 'raceId' IN (Select 'raceId' as race FROM " \
                "(SELECT 'raceId' FROM RESULTS WHERE position is Null OR 'positionText' = 'R') as NewTab)"
        self.db_cursor.execute(query)
        self.db_connection.commit()
        elapsed_time = time.perf_counter() - start_time
        if stdout:
            print(f"Update laptimes of disqualified drivers, time: {elapsed_time}s")
        return ["UPDATE LAPTIMES OF DISQUALIFIED DRIVERS", "-", elapsed_time]
