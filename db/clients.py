from .loader import Loader

class ClientDB:

    @staticmethod
    def get_clients(path):
        return Loader.file_loader(path)

    @staticmethod
    def include_register(path, data):
        clients = ClientDB.get_clients(path)
        clients.append(data)
        Loader.update_file(clients, "clients")
        return clients