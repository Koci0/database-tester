import docker


class DatabaseContainer:
    client = docker.from_env()

    def __init__(self):
        self.containers = {}
        """IP: container"""

    def add_container(self) -> None:
        """Creates a container"""
        pass

    def stop_container(self, container) -> None:
        """Stops a given container"""
        pass

    def stop_all_containers(self) -> None:
        """Stops all the containers from the 'containers' dict"""
        pass

    def cleanup(self) -> None:
        """Performs docker client cleanup"""
        self.client.containers.prune()

    @staticmethod
    def get_fresh_attrs(container):
        """Returns refreshed attributes of a given container"""
        container.reload()
        return container.attrs
