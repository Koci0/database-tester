import os
import time
from time import sleep
from typing import List

import pandas as pd
import pymongo
from pymongo import MongoClient

import const
import db_const
from modules.database_container import DatabaseContainer
from modules.helpers import MongoHelpers


class Mongo(DatabaseContainer):
    master_container = None
    db_client = None
    database = None

    def __init__(self):
        super().__init__()

    def add_container(self) -> None:
        index = len(self.containers) + 1
        container_name = f"mongo-{index}"
        host_port = str(27017)
        container_image = "mongo:5.0.8"

        print(f"Mongo #{index} is starting...")

        container = self.client.containers.run(
            name=container_name,
            image=container_image,
            ports={27017: host_port},
            privileged=True,
            detach=True,
            environment=[f"MONGO_INITDB_ROOT_USERNAME={const.MONGO_USER}",
                         f"MONGO_INITDB_ROOT_PASSWORD={const.MONGO_PASSWORD}"]
        )

        container_ip = self.get_fresh_attrs(container)['NetworkSettings']['IPAddress']
        self.containers[container_ip] = container
        print(f"Mongo {container.id} started on IP {container_ip}.")
        self.master_container = container

        print("Waiting until connection is established", end="")
        while not self._is_connection_established():
            print(".", end="")
            sleep(1)
        print()
        print("Connection established.")

    def stop_container(self, container) -> None:
        container.stop()
        print(f"Mongo {container.id} stopped.")

    def stop_all_containers(self) -> None:
        for container in self.containers.values():
            self.stop_container(container)
        self.containers.clear()

    def execute_query(self, sql, stdout=True) -> int:
        cmd = f"mongosh --eval '{sql}'"
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
        sql_list = r"help"
        exit_code = self.execute_query(sql_list, stdout=False)
        if exit_code == 0:
            return True
        return False

    def initialize_database(self, stdout=False):
        self.db_client = MongoClient(const.MONGO_CONNECTION_STRING, username=const.MONGO_USER,
                                     password=const.MONGO_PASSWORD)
        self.database = self.db_client[const.MONGO_DATABASE]
        csv_files = MongoHelpers.get_list_of_script_files()
        results = []
        start_time = time.perf_counter()
        for file in csv_files:
            df = pd.read_csv(os.path.join(const.MONGO_CSV_FILES, file), sep=';')
            data = df.to_dict('records')
            collection_name = self.database[file.replace(".csv", "")]
            collection_name.insert_many(data)
            if stdout:
                print(f"Inserted collection {collection_name.name}")
        end_time = time.perf_counter()
        result_time = end_time - start_time
        results.append(("INSERT", "-", result_time))
        return results

    def select_all_data_from_columns(self, stdout=False) -> List:
        """Select All Data from Columns By Column Name"""
        results = []
        for key, value in db_const.COLLECTION_NAMES.items():
            if key == "JOINED":
                continue
            start_time = time.perf_counter()
            collection = self.database[value]
            collection.find()
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            if stdout:
                print(f"Time to select all rows from collection: {value} time: {elapsed_time}")
            results.append(("SELECT ALL DATA FROM COLUMNS", key, elapsed_time))
        return results

    def select_races_data(self, stdout=False) -> List:
        """Select All Data from Races Table"""
        start_time = time.perf_counter()
        query = [
            {'$lookup': {'from': 'drivers', 'localField': "driverId", 'foreignField': "driverId", 'as': "driverData"}},
            {'$unwind': "$driverData"},
            {'$lookup': {'from': "races", 'localField': "raceId", 'foreignField': "raceId", 'as': "raceData"}},
            {'$unwind': "$raceData"},
            {'$lookup': {'from': "constructors", 'localField': "constructorId", 'foreignField': "constructorId",
                         'as': "constructorData"}},
            {'$unwind': "$constructorData"},
            {'$lookup': {'from': "status", 'localField': "statusId", 'foreignField': "statusId", 'as': "statusData"}},
            {'$unwind': "$statusData"}
        ]
        self.database.results.aggregate(query)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        if stdout:
            print(f"Find data from Results with related collections, Time: {elapsed_time}")
        return ["SELECT RACES DATA", "-", elapsed_time]

    def select_longest_lap(self, stdout=False) -> List:
        """Select Longest Lap from laptimes table"""
        start_time = time.perf_counter()
        self.database.laptimes.find().sort([('milliseconds', pymongo.DESCENDING)]).limit(1)
        elapsed_time = time.perf_counter() - start_time
        if stdout:
            print(f"Select longest lap time, Time: {elapsed_time}")
        return ["SELECT LONGEST LAP", "-", elapsed_time]

    def select_driver_with_most_1st_positions(self, stdout=False) -> List:
        """Select Driver with the most 1st positions"""
        start_time = time.perf_counter()
        query = [
            {
                '$match': {'position': {'$eq': '1'}}
            },
            {
                '$group': {'_id': "$driverId", 'count': {'$sum': '1'}}
            }
        ]
        self.database.qualifying.aggregate(query)
        elapsed_time = time.perf_counter() - start_time
        if stdout:
            print(f"Select driver with most 1st positions, time: {elapsed_time}s")
        return ["SELECT DRIVER WITH MOST 1st POSITIONS", "-", elapsed_time]

    def remove_results(self, stdout=False) -> List:
        """Remove Results of Drivers that got position lower than 30 more than 10 times ~7k rows affected"""
        query = [
            {
                '$match': {'position': {'$lt': 30}}
            },
            {
                '$group':
                    {
                        '_id': '$driverId',
                        'count': {'$sum': 1}
                    }
            },
            {
                '$match': {'count': {'$gt': 5}}
            },
            {
                '$group':
                    {
                        '_id': "$_id"
                    }
            }
        ]
        start_time = time.perf_counter()
        ids = list(self.database.qualifying.aggregate(query))
        elapsed_time = time.perf_counter() - start_time

        drivers_ids = [d["_id"] for d in ids]

        start_time = time.perf_counter()
        self.database.results.delete_many({'driverId': {'$in': drivers_ids}})
        elapsed_time += time.perf_counter() - start_time
        if stdout:
            print(f"Removing results, time: {elapsed_time}s")
        return ["REMOVE RESULTS FOR SPECIFIC DRIVERS", "-", elapsed_time]

    def update_laptimes(self, stdout=False) -> List:
        """Update lap times for races where drivers where disqualified """
        query = [
            {'$match':
                {
                    '$or': [{'position': 'null'}, {'positionText': 'R'}]
                }
            },
            {'$project':
                {
                    '_id': 'false',
                    'driverId': '$driverId',
                    'raceId': '$raceId'
                }
            }
        ]
        start_time = time.perf_counter()
        results = list(self.database.results.aggregate(query))
        elapsed_time = time.perf_counter() - start_time
        driverIds = [d["driverId"] for d in results]
        raceIds = [d["raceId"] for d in results]
        myquery = {'$or': [{'driverId': {'$in': driverIds}}, {'raceId': {'$in': raceIds}}]}
        update_query = {
            '$inc': {'milliseconds': 10000000},
            '$set': {
                'position': 100,
                'time': 'UPDATED COLUMN'
            },
        }
        start_time = time.perf_counter()
        self.database.laptimes.update_many(myquery, update_query)
        elapsed_time += (time.perf_counter() - start_time)
        if stdout:
            print(f"Update laptimes of disqualified drivers, time: {elapsed_time}s")
        return ["UPDATE LAPTIMES OF DISQUALIFIED DRIVERS", "-", elapsed_time]