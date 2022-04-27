import os
from typing import List

import pandas

from const import DATA_PATH, SEPARATOR
from modules.cassandra import Cassandra


class Tester:
    csv_filenames = os.listdir(DATA_PATH)
    csv_data = {}
    """filename: Dataframe"""

    def __init__(self, data_path=DATA_PATH) -> None:
        self.data_path = data_path
        self._cassandra = None
        self._import_all_data_from_csv(self.csv_filenames)

    def run(self, automatic):
        self.run_cassandra(automatic)
        pass

    def run_cassandra(self, automatic):
        self._cassandra = Cassandra()
        try:
            self._start_cassandra(n=3)
            print("Tester for Cassandra finished.")
            if not automatic:
                self._wait_for_input()
        finally:
            self._stop_cassandra()
            print("Cleanup for Cassandra finished.")

    def _start_cassandra(self, n=3):
        for i in range(n):
            self._cassandra.add_container()

    def _stop_cassandra(self):
        self._cassandra.stop_all_containers()
        self._cassandra.cleanup()
        self._cassandra = None

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
