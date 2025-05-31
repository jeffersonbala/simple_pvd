import sv_ttk
from tkinter import ttk

from view.base import BaseView

class HomeView(BaseView):

    def __init__(self):
        super().__init__()

        self.create_widgets()

        self.visible = True


    def create_widgets(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        icon_label = ttk.Label(self, text="🛒", font=("Source Code Mono", 64))
        icon_label.grid(row=0, column=0, columnspan=3, pady=20)

        title_label = ttk.Label(self, text="Bem Vindo ao Simple PDV!", font=("Source Code Mono", 32))
        title_label.grid(row=1, column=0, columnspan=3, pady=20)

        sales_button = ttk.Button(self, text="Vendas")
        sales_button.grid(row=2, column=0, padx=10, pady=10)

        products_button = ttk.Button(self, text="Produtos")
        products_button.grid(row=2, column=1, padx=10, pady=10)

        clients_button = ttk.Button(self, text="Clientes")
        clients_button.grid(row=2, column=2, padx=10, pady=10)

        exit_button = ttk.Button(self, text="Sair", command=self.quit)
        exit_button.grid(row=3, column=0, columnspan=3, pady=30)

    def get_sales_button(self):
        return self.grid_slaves(row=2, column=0)[0]
    
    def get_products_button(self):
        return self.grid_slaves(row=2, column=1)[0]
    
    def get_clients_button(self):
        return self.grid_slaves(row=2, column=2)[0]
