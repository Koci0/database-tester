import docker

from modules.database_container import DatabaseContainer

client = docker.from_env()


class Cassandra(DatabaseContainer):
    MEM_LIMIT = "1g"

    # IP: container
    containers = {}

    def add_container(self) -> None:
        index = len(self.containers) + 1
        container_name = f"cassandra-{index}"
        host_port = str(9042 + index - 1)
        container_image = "cassandra:4.0"

        print(f"Cassandra #{index} is starting...")

        if index == 1:
            container = client.containers.run(
                name=container_name,
                image=container_image,
                ports={9042: host_port},
                mem_limit=self.MEM_LIMIT,
                detach=True,
            )
        else:
            seeds = ','.join([ip_address for ip_address in self.containers.keys()])
            container = client.containers.run(
                name=container_name,
                image=container_image,
                ports={9042: host_port},
                mem_limit=self.MEM_LIMIT,
                detach=True,
                environment=[f"CASSANDRA_SEEDS={seeds}"],
            )

        container_ip = self.get_fresh_attrs(container)['NetworkSettings']['IPAddress']
        self.containers[container_ip] = container
        print(f"Cassandra {container.id} started on IP {container_ip}.")

    def stop_container(self, container) -> None:
        container.stop()
        print(f"Cassandra {container.id} stopped.")

    def stop_all_containers(self) -> None:
        for container in self.containers.values():
            self.stop_container(container)
