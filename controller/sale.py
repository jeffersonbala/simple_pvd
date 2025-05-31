from view.sale import SaleView

class SaleController:

    def __init__(self, view):
        self.view : SaleView = view

        self.add_events()

    def add_events(self):
        self.view.get_close_button().configure(command=self.view.destroy)

        
        

 


