import os

ROOT_PATH = os.path.abspath(os.path.curdir)
DATA_PATH = os.path.join(ROOT_PATH, "data")
SEPARATOR = 30 * "#"

CASSANDRA_KEYSPACE = "f1_data"
CASSANDRA_SCRIPTS_FILE_DIR = os.path.join(DATA_PATH, "cassandra_queries")

POSTGRES_USER = "root"
POSTGRES_PASSWORD = "root"
POSTGRES_HOST = "localhost"
POSTGRES_DATABASE = "postgres"
POSTGRES_PORT = "5432"
POSTGRES_SCRIPTS_FILE_DIR = os.path.join(DATA_PATH, "postgresql_queries")

MONGO_USER = "mongoUser"
MONGO_PASSWORD = "password"
MONGO_DATABASE = "Formula1DB"
MONGO_CONNECTION_STRING = "mongodb://localhost:27017"
MONGO_CSV_FILES = os.path.join(DATA_PATH, "csv_files")
