import os
import time
from typing import List

import pandas

import const
from const import DATA_PATH, SEPARATOR
from modules.database_container import DatabaseContainer
from modules.cassandra import Cassandra
from modules.mongo import Mongo
from modules.postgres import Postgres


def run_test(container: DatabaseContainer, sql):
    # TODO: Measure delay for docker exec and subtract it from the result
    begin_time = time.time()
    container.execute_query(sql)
    elapsed_time = time.time() - begin_time
    print(f"Finished in {elapsed_time}s")


class Tester:
    csv_filenames = os.listdir(DATA_PATH)
    csv_data = {}
    """filename: Dataframe"""

    # TODO: create multiple containers
    n_cassandra_containers = 1

    def __init__(self, data_path=DATA_PATH) -> None:
        self.data_path = data_path
        self._cassandra = None
        self._postgres = None
        self._mongo = None
        self._import_all_data_from_csv(self.csv_filenames)

    def run(self, automatic):
        self.run_cassandra(automatic)
        print(f"\n{const.SEPARATOR}\n", end="")
        self.run_postgres(automatic)
        print(f"\n{const.SEPARATOR}\n", end="")
        self.run_mongo(automatic)

    def run_cassandra(self, automatic):
        self._cassandra = Cassandra()
        try:
            print("Starting Cassandra...")
            self._start_cassandra(n=self.n_cassandra_containers)
            print("Cassandra has started.")
            if not automatic:
                self._wait_for_input()

            print("Testing Cassandra...")
            self._test_cassandra()
            print("Cassandra finished testing.")
            if not automatic:
                self._wait_for_input()
        finally:
            print("Stopping Cassandra...")
            self._stop_cassandra()
            print("Cassandra has stopped.")

    def _start_cassandra(self, n):
        for i in range(n):
            self._cassandra.add_container()

    def _test_cassandra(self):
        run_test(self._cassandra, "help")

    def _stop_cassandra(self):
        self._cassandra.stop_all_containers()
        self._cassandra.cleanup()
        self._cassandra = None

    def run_postgres(self, automatic):
        self._postgres = Postgres()
        try:
            print("Starting Postgres...")
            self._postgres.add_container()
            print("Postgres has started.")
            if not automatic:
                self._wait_for_input()

            print("Testing Postgres...")
            self._test_postgres()
            print("Postgres finished testing.")
            if not automatic:
                self._wait_for_input()
        finally:
            print("Stopping Postgres...")
            self._stop_postgres()
            print("Postgres has stopped.")

    def _test_postgres(self):
        run_test(self._postgres, r"\\help")

    def _stop_postgres(self):
        self._postgres.stop_all_containers()
        self._postgres.cleanup()
        self._postgres = None

    def run_mongo(self, automatic):
        self._mongo = Mongo()
        try:
            print("Starting Mongo...")
            self._mongo.add_container()
            print("Mongo has started.")
            if not automatic:
                self._wait_for_input()

            print("Testing Mongo...")
            self._test_mongo()
            print("Mongo finished testing.")
            if not automatic:
                self._wait_for_input()
        finally:
            print("Stopping Mongo...")
            self._stop_mongo()
            print("Mongo has stopped.")

    def _test_mongo(self):
        run_test(self._mongo, r"help")

    def _stop_mongo(self):
        self._mongo.stop_all_containers()
        self._mongo.cleanup()
        self._mongo = None

    def _import_data_from_csv(self, filename: str) -> None:
        """Loads data from a given CSV file in `data` directory to `data_path` dict"""
        absolute_path = os.path.join(self.data_path, filename)
        data = pandas.read_csv(absolute_path)
        self.csv_data[filename] = data

    def _import_all_data_from_csv(self, filenames: List[str]) -> None:
        """Loads data from all given CSV files `data` directory"""
        for filename in filenames:
            self._import_data_from_csv(filename)
        print(f"Loaded {len(self.csv_data)} csv files.")

    def _print_csv_data(self) -> None:
        """Prints head (5 rows) from all csv files loaded as DataFrames"""
        for filename, dataframe in self.csv_data.items():
            print(f"{filename}:")
            print(dataframe.head())
            print(SEPARATOR)

    @staticmethod
    def _wait_for_input():
        input("Press Enter to continue...")
