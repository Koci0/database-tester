import os

import psycopg2

import const


class PostgresHelpers:

    @staticmethod
    def get_db_cursor(db_connection):
        return db_connection.cursor()

    @staticmethod
    def get_list_of_script_files():
        list_of_files = sorted(os.listdir(const.POSTGRES_SCRIPTS_FILE_DIR))
        return list_of_files

    @staticmethod
    def get_connection_to_database():
        conn = None
        try:
            print("Connecting to PostgresSQL database...")
            conn = psycopg2.connect(
                host=const.POSTGRES_HOST,
                database=const.POSTGRES_DATABASE,
                user=const.POSTGRES_USER,
                password=const.POSTGRES_PASSWORD,
                port=const.POSTGRES_PORT
            )
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                print("Connected to PostgresSQL database.")
            return conn

    @staticmethod
    def close_connection_to_database(connection):
        if connection is not None:
            try:
                connection.close()
                print("Database connection closed.")
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
