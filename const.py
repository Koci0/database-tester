import os

ROOT_PATH = os.path.abspath(os.path.curdir)
DATA_PATH = os.path.join(ROOT_PATH, "data")
SEPARATOR = 30 * "#"

POSTGRES_USER = "root"
POSTGRES_PASSWORD = "root"
POSTGRES_HOST = "localhost"
POSTGRES_DATABASE = "postgres"
POSTGRES_PORT = "5432"
POSTGRES_SCRIPTS_FILE_DIR = os.path.join(DATA_PATH, "postgresql_queries")
