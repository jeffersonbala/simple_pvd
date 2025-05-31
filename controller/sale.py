from view.sale import SaleView

class SaleController:

    def __init__(self, view):
        self.view : SaleView = view

        self.add_events()

    def add_events(self):
        self.view.get_back_button().configure(command=self.go_back)

    def go_back(self):
        self.view.parent.toggle_visibility()
        self.view.toggle_visibility()
        self.view.destroy()

