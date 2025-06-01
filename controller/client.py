from view.client import ClientView

class ClientController:

    def __init__(self, view):
        self.view = view

        self.add_events()

    def add_events(self):
        self.view.get_add_client_button().configure(command=self.add_client)
        self.view.get_edit_client_button().configure(command=self.edit_client)

    def add_client(self):
        pass

    def edit_client(self):
        pass