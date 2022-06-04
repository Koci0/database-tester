from tabulate import tabulate

import const
from modules.cassandra import Cassandra
from modules.mongo import Mongo
from modules.postgres import Postgres


class Tester:
    # TODO: create multiple containers
    n_cassandra_containers = 1

    def __init__(self, data_path=const.DATA_PATH) -> None:
        self.data_path = data_path
        self._cassandra = None
        self._postgres = None
        self._mongo = None
        self.results = {
            "Cassandra": [],
            "Postgres": [],
            "Mongo": []
        }

    def run(self, automatic):
        # self.run_cassandra(automatic)
        # print(f"\n{const.SEPARATOR}\n", end="")
        self.run_postgres(automatic)
        print(f"\n{const.SEPARATOR}\n", end="")
        self.run_mongo(automatic)
        print(f"\n{const.SEPARATOR}\n", end="")
        self._print_results()

    def run_cassandra(self, automatic):
        self._cassandra = Cassandra()
        try:
            print("> Starting Cassandra...")
            self._start_cassandra(n=self.n_cassandra_containers)
            print("> Cassandra has started.")

            print("> Initializing Cassandra...")
            self.results["Cassandra"].extend(self._cassandra.initialize_database())
            print("> Cassandra has initialized.")

            if not automatic:
                self._wait_for_input()

            print("> Testing Cassandra...")
            self._test_cassandra()
            print("> Cassandra finished testing.")

            if not automatic:
                self._wait_for_input()
        finally:
            print("> Stopping Cassandra...")
            self._stop_cassandra()
            print("> Cassandra has stopped.")

    def _start_cassandra(self, n):
        for i in range(n):
            self._cassandra.add_container()

    def _test_cassandra(self):
        self.results["Cassandra"].extend(self._cassandra.select_all_data_from_columns())
        self.results["Cassandra"].append(self._cassandra.select_races_data())
        self.results["Cassandra"].append(self._cassandra.select_longest_lap())
        self.results["Cassandra"].append(self._cassandra.select_driver_with_most_1st_positions())

    def _stop_cassandra(self):
        self._cassandra.stop_all_containers()
        self._cassandra.cleanup()
        self._cassandra = None

    def run_postgres(self, automatic):
        self._postgres = Postgres()
        try:
            print("> Starting Postgres...")
            self._postgres.add_container()
            print("> Postgres has started.")

            print("> Initializing Postgres...")
            self.results["Postgres"].extend(self._postgres.initialize_database())
            print("> Postgres has initialized.")

            if not automatic:
                self._wait_for_input()

            print("> Testing Postgres...")
            self._test_postgres()
            print("> Postgres has finished testing.")

            if not automatic:
                self._wait_for_input()
        finally:
            print("> Stopping Postgres...")
            self._stop_postgres()
            print("> Postgres has stopped.")

    def _test_postgres(self):
        self.results["Postgres"].extend(self._postgres.select_all_data_from_columns())
        self.results["Postgres"].append(self._postgres.select_races_data())
        self.results["Postgres"].append(self._postgres.select_longest_lap())
        self.results["Postgres"].append(self._postgres.select_driver_with_most_1st_positions())
        self.results["Postgres"].append(self._postgres.update_laptimes())
        self.results["Postgres"].append(self._postgres.remove_results())

    def _stop_postgres(self):
        self._postgres.stop_all_containers()
        self._postgres.cleanup()
        self._postgres = None

    def run_mongo(self, automatic):
        self._mongo = Mongo()
        try:
            print("> Starting Mongo...")
            self._mongo.add_container()
            print("> Mongo has started.")

            print("> Initializing Mongo...")
            self.results["Mongo"].extend(self._mongo.initialize_database())
            print("> Mongo has initialized.")

            if not automatic:
                self._wait_for_input()

            print("> Testing Mongo...")
            self._test_mongo()
            print("> Mongo finished testing.")

            if not automatic:
                self._wait_for_input()
        finally:
            print("> Stopping Mongo...")
            self._stop_mongo()
            print("> Mongo has stopped.")

    def _test_mongo(self):
        self.results["Mongo"].extend(self._mongo.select_all_data_from_columns())
        self.results["Mongo"].append(self._mongo.select_races_data())
        self.results["Mongo"].append(self._mongo.select_longest_lap())
        self.results["Mongo"].append(self._mongo.select_driver_with_most_1st_positions())
        self.results["Mongo"].append(self._mongo.update_laptimes())
        self.results["Mongo"].append(self._mongo.remove_results())

    def _stop_mongo(self):
        self._mongo.db_client.close()
        self._mongo.stop_all_containers()
        self._mongo.cleanup()
        self._mongo = None

    def _print_results(self):
        for database in self.results.keys():
            print(f"Results for {database}")
            print(tabulate(self.results[database]))

    @staticmethod
    def _wait_for_input():
        input("Press Enter to continue...")
