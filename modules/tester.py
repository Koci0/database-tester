from modules.cassandra import Cassandra


class Tester:

    def __init__(self) -> None:
        self.cassandra = Cassandra()

    def run(self):
        try:
            self.start_cassandra(n=3)
            print("Tester for Cassandra finished.")
        finally:
            self.stop_cassandra()
            print("Cleanup for Cassandra finished.")

    def start_cassandra(self, n=3):
        for i in range(n):
            self.cassandra.add_container()

    def stop_cassandra(self):
        self.cassandra.stop_all_containers()
        self.cassandra.cleanup()
