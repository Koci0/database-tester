from time import sleep

from modules.database_container import DatabaseContainer


class Cassandra(DatabaseContainer):
    # TODO: limit memory usage
    mem_limit = "4g"
    master_container = None

    def __init__(self):
        super().__init__()

    def add_container(self) -> None:
        index = len(self.containers) + 1
        container_name = f"cassandra-{index}"
        host_port = str(9042 + index - 1)
        container_image = "cassandra:4.0"

        print(f"Cassandra #{index} is starting...")

        if index == 1:
            container = self.client.containers.run(
                name=container_name,
                image=container_image,
                ports={9042: host_port},
                privileged=True,
                detach=True,
            )
        else:
            seeds = ','.join([ip_address for ip_address in self.containers.keys()])
            container = self.client.containers.run(
                name=container_name,
                image=container_image,
                ports={9042: host_port},
                privileged=True,
                detach=True,
                environment=[f"CASSANDRA_SEEDS={seeds}"],
            )

        container_ip = self.get_fresh_attrs(container)['NetworkSettings']['IPAddress']
        self.containers[container_ip] = container
        print(f"Cassandra {container.id} started on IP {container_ip}.")
        if self.master_container is None:
            self.master_container = container
            print(f"Master Cassandra container is {container_ip}.")

        print("Waiting until connection is established", end="")
        while not self._is_connection_established():
            print(".", end="")
            sleep(1)
        print()
        print("Connection established.")

    def stop_container(self, container) -> None:
        container.stop()
        print(f"Cassandra {container.id} stopped.")

    def stop_all_containers(self) -> None:
        for container in self.containers.values():
            self.stop_container(container)
        self.containers.clear()

    def execute_query(self, sql, stdout=True) -> int:
        cmd = f"cqlsh -e {sql}"
        exit_code, output = self.master_container.exec_run(cmd, privileged=True)
        if stdout:
            if exit_code != 0:
                msg = "[Error]"
            else:
                msg = "[Success]"
            print(f"\t{output.decode('utf-8')}")
            print(f"{msg} Command '{cmd}' returned code {exit_code}.")

        return exit_code

    def _is_connection_established(self) -> bool:
        sql = "help"
        exit_code = self.execute_query(sql, stdout=False)
        if exit_code == 0:
            return True
        return False
