from time import sleep

from modules.database_container import DatabaseContainer


class Mongo(DatabaseContainer):
    master_container = None

    def __init__(self):
        super().__init__()

    def add_container(self) -> None:
        index = len(self.containers) + 1
        container_name = f"mongo-{index}"
        host_port = str(9042)
        container_image = "mongo:5.0.8"

        print(f"Mongo #{index} is starting...")

        container = self.client.containers.run(
            name=container_name,
            image=container_image,
            # ports={8080: host_port},
            privileged=True,
            detach=True
        )

        container_ip = self.get_fresh_attrs(container)['NetworkSettings']['IPAddress']
        self.containers[container_ip] = container
        print(f"Mongo {container.id} started on IP {container_ip}.")
        self.master_container = container

        print("Waiting until connection is established", end="")
        while not self._is_connection_established():
            print(".", end="")
            sleep(1)
        print()
        print("Connection established.")

    def stop_container(self, container) -> None:
        container.stop()
        print(f"Mongo {container.id} stopped.")

    def stop_all_containers(self) -> None:
        for container in self.containers.values():
            self.stop_container(container)
        self.containers.clear()

    def execute_query(self, sql, stdout=True) -> int:
        cmd = f"mongosh --eval '{sql}'"
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
        sql_list = r"help"
        exit_code = self.execute_query(sql_list, stdout=False)
        if exit_code == 0:
            return True
        return False
