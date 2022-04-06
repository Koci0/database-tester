import docker

client = docker.from_env()


class DatabaseContainer:
    # id: container
    containers = {}

    def add_container(self) -> None:
        """Creates a container"""
        pass

    def stop_container(self, container) -> None:
        """Stops a given container"""
        pass

    def stop_all_containers(self) -> None:
        """Stops all of the containers from the 'containers' dict"""
        pass

    @staticmethod
    def cleanup() -> None:
        """Performs docker client cleanup"""
        client.containers.prune()

    @staticmethod
    def get_fresh_attrs(container):
        """Returns refreshed attributes of a given container"""
        container.reload()
        return container.attrs
