import os
from time import sleep, time

import psycopg2
from psycopg2 import OperationalError

SCRIPTS_FILE_DIR = "postgresql_queries/"


def get_db_cursor(db_connection):
    return db_connection.cursor()


def get_list_of_script_files():
    list_of_files = sorted(filter(lambda x: os.path.isfile(os.path.join(SCRIPTS_FILE_DIR, x)),
                                  os.listdir(SCRIPTS_FILE_DIR)))
    return list_of_files


def get_connection_to_database():
    conn = None
    try:
        print("Connection to PostgresSQL database...")
        conn = psycopg2.connect(
            host="postgres_db_host",
            database="postgres",
            user="postgres",
            password="postgres",
            port="5432"
        )
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return conn


def initialize_database_tables():
    db_connection = get_connection_to_database()
    db_cursor = get_db_cursor(db_connection)
    sql_files = get_list_of_script_files()
    for file in sql_files:
        print(f"Running queries from file {file}")
        sql_file = open(SCRIPTS_FILE_DIR + file, encoding="utf-8")
        sql_as_string = sql_file.read()
        start_time = time()
        try:
            db_cursor.execute(sql_as_string)
        except OperationalError as msg:
            print(f"Command skipped: {msg}")
        except psycopg2.DatabaseError as msg:
            print(f"Table exists: {msg}")
        db_connection.commit()
        end_time = time()
        result_time = end_time - start_time
        print(f"Time to insert data into table {file.replace('.sql', '')} = {result_time}")


if __name__ == "__main__":
    sleep(10)
    initialize_database_tables()
