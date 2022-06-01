import time

import pymongo
from pymongo import MongoClient

from db_constants import *

DATABASE_NAME = "Formula1DB"
CONNECTION_STRING = "mongodb://mongo_db_host:27017"


def get_connection_to_database():
    client = MongoClient(CONNECTION_STRING, username='mongoUser', password='password')
    return client[DATABASE_NAME]


def close_connection(client):
    client.close()


# Select All Data from Columns By Column Name
def select_all_data_from_collections(client):
    start_time1 = time.perf_counter()
    for key, values in COLLECTION_NAMES.items():
        start_time = time.perf_counter()
        collection = client[values]
        collection.find()
        end_time = time.perf_counter()
        result_time = end_time - start_time
        print(f"Time to select all rows from collection: {values} time: {result_time}")
    end_time1 = time.perf_counter()
    result_time = end_time1 - start_time1
    print(f"Time to get all data from database: {result_time}")

    # Select All Data from Races Table


def select_races_data(client):
    start_time = time.time()
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
    client.results.aggregate(query)
    end_time = time.time()
    result_time = end_time - start_time
    print(f"Find data from Results with related collections, Time: {result_time}")


# Select Longest Lap from laptimes table
def select_longest_lap(client):
    start_time = time.time()
    client.laptimes.find().sort([('milliseconds', pymongo.DESCENDING)]).limit(1)
    end_time = time.time()
    result_time = end_time - start_time
    print(f"Select longest lap time, Time: {result_time}")


# Select Driver with the most 1st positions
def select_driver_with_most_1st_positions(client):
    start_time = time.time()
    query = [
        {
            '$match': {'position': {'$eq': '1'}}
        },
        {
            '$group': {'_id': "$driverId", 'count': {'$sum': '1'}}
        }
    ]
    client.qualifying.aggregate(query)
    end_time = time.time()
    result_time = end_time - start_time
    print(f"Select driver with most 1st positions, Time: {result_time}")


if __name__ == "__main__":
    time.sleep(30)
    client = get_connection_to_database()

    select_all_data_from_collections(client)

    select_races_data(client)

    select_longest_lap(client)

    select_driver_with_most_1st_positions(client)
    # close_connection(client)
