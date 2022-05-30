from time import sleep, time
import pandas as pd
import json

from pymongo import MongoClient
import pymongo
import os

CSV_FILE_DIR = "tables_csv/"
DATABASE_NAME = "Formula1DB"
CONNECTION_STRING = "mongodb://mongo_db_host:27017"


def get_list_of_script_files():
    list_of_files = sorted(filter(lambda x: os.path.isfile(os.path.join(CSV_FILE_DIR, x)),
                                  os.listdir(CSV_FILE_DIR)))
    return list_of_files


def initialize_database():
    client = MongoClient(CONNECTION_STRING, username='mongoUser', password='password')
    database = client[DATABASE_NAME]
    csv_files = get_list_of_script_files()
    for file in csv_files:
        df = pd.read_csv(CSV_FILE_DIR+file, sep=';')
        data = df.to_dict('records')
        collectionName = database[file.replace(".csv", "")]
        start_time = time()
        collectionName.insert_many(data)
        end_time = time()
        result_time = end_time - start_time
        print(f"Time to insert data into collection {collectionName.name} = {result_time}")
    pass


if __name__ == "__main__":
    sleep(10)
    initialize_database()
