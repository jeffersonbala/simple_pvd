import sv_ttk
from tkinter import ttk

from view.base import BaseView

class SaleView(BaseView):

    def __init__(self, parent: BaseView):
        super().__init__()

        self.create_widgets()

        self.parent = parent

        self.visible = True

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        icon_label = ttk.Label(self, text="💰", font=("Source Code Mono", 64))
        icon_label.grid(row=0, column=0, columnspan=3, pady=20)

        title_label = ttk.Label(self, text="Vendas", font=("Source Code Mono", 32))
        title_label.grid(row=1, column=0, columnspan=3, pady=20)

        new_sale_button = ttk.Button(self, text="Nova Venda")
        new_sale_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        back_button = ttk.Button(self, text="Fechar")
        back_button.grid(row=2, column=2, padx=10, pady=10)


    def get_close_button(self):
        return self.grid_slaves(row=2, column=2)[0]
      
    def get_new_sale_button(self):
        return self.grid_slaves(row=2, column=0)[0]
    
