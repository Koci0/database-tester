import psycopg2

from db_constants import *
import time


def get_connection_to_database():
    conn = None
    try:
        print("Connection to PostgresSQL database...")
        conn = psycopg2.connect(
            host="postgres_db",
            database="postgres",
            user="postgres",
            password="postgres",
            port="5432"
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return conn


def close_connection_to_database(connection):
    if connection is not None:
        try:
            connection.close()
            print("Database connection closed. ")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)


def get_db_cursor(db_connection):
    return db_connection.cursor()


# Select All Data from Columns By Column Name
def select_all_data_from_columns(cursor):
    for key, value in TABLES_NAMES.items():
        start_time = time.time()
        query = f'SELECT * from {value}'
        cursor.execute(query)
        end_time = time.time()
        result_time = end_time - start_time
        print(f"Time to select all rows from column: {key} time: {result_time}")


# Select All Data from Races Table
def select_races_data(cursor):
    start_time = time.time()
    query = f'SELECT * from {TABLES_NAMES["RESULTS"]}' \
    f' inner join {TABLES_NAMES["RACES"]} r on r."{RACES_COLUMNS["RACE_ID"]}" = {TABLES_NAMES["RESULTS"]}."{RESULTS_COLUMNS["RACE_ID"]}"' \
    f' inner join {TABLES_NAMES["DRIVERS"]} d on d."{DRIVER_COLUMNS["DRIVER_ID"]}" = {TABLES_NAMES["RESULTS"]}."{RESULTS_COLUMNS["DRIVER_ID"]}"' \
    f' inner join {TABLES_NAMES["CONSTRUCTORS"]} c on c."{CONSTRUCTORS_COLUMNS["CONSTRUCTOR_ID"]}" = {TABLES_NAMES["RESULTS"]}."{RESULTS_COLUMNS["CONSTRUCTOR_ID"]}"' \
    f' inner join {TABLES_NAMES["STATUS"]} s on s."{STATUS_COLUMNS["STATUS_ID"]}" = {TABLES_NAMES["RESULTS"]}."{RESULTS_COLUMNS["STATUS_ID"]}"'

    cursor.execute(query)
    end_time = time.time()
    result_time = end_time - start_time
    print(f"All data from {TABLES_NAMES['RESULTS']} with related columns, Time: {result_time}")


# Select Longest Lap from laptimes table
def select_longest_lap(cursor):
    start_time = time.time()
    query = f'SELECT * from {TABLES_NAMES["LAPTIMES"]}' \
            f' WHERE {LAPTIMES_COLUMNS["MILLISECONDS"]} = ' \
            f'(SELECT MAX({LAPTIMES_COLUMNS["MILLISECONDS"]}) FROM {TABLES_NAMES["LAPTIMES"]})'
    cursor.execute(query)
    end_time = time.time()
    result_time = end_time - start_time
    print(f"Select longest lap time, Time: {result_time}")


# Select Driver with the most 1st positions
def select_driver_with_most_1st_positions(cursor):
    start_time = time.time()
    query = f'SELECT * FROM {TABLES_NAMES["DRIVERS"]} where ' \
            f'"{DRIVER_COLUMNS["DRIVER_ID"]}" = (SELECT "{DRIVER_COLUMNS["DRIVER_ID"]}" as driver FROM (SELECT ' \
            f'"{DRIVER_COLUMNS["DRIVER_ID"]}", count( *) cnt, rank() over(ORDER BY count(*) DESC) FROM {TABLES_NAMES["QUALIFYING"]} ' \
            f'WHERE {QUALIFYING_COLUMNS["POSITION"]} = 1 GROUP BY "{DRIVER_COLUMNS["DRIVER_ID"]}") a ' \
            f'WHERE rank = 1)'
    cursor.execute(query)
    end_time = time.time()
    result_time = end_time - start_time
    print(f"Select driver with most 1st positions, Time: {result_time}")


if __name__ == '__main__':
    time.sleep(120)
    connection = get_connection_to_database()
    cursor = get_db_cursor(connection)

    select_all_data_from_columns(cursor)

    select_races_data(cursor)

    select_longest_lap(cursor)

    select_driver_with_most_1st_positions(cursor)


