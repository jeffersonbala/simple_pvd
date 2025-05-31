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

        

        icon_label = ttk.Label(self, text="💰 Vendas", font=("Source Code Mono", 64))
        icon_label.grid(row=0, column=0, columnspan=3, pady=20)

        new_sale_button = ttk.Button(self, text="Nova Venda")
        new_sale_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        back_button = ttk.Button(self, text="Fechar")
        back_button.grid(row=2, column=2, padx=10, pady=10)

        self.create_table()


    def get_close_button(self):
        return self.grid_slaves(row=2, column=2)[0]
      
    def get_new_sale_button(self):
        return self.grid_slaves(row=2, column=0)[0]
    
    def create_table(self):

        data = [
            ("30/05/2025", "Arroz", 10),
            ("30/05/2025", "Feijão", 5),
            ("30/05/2025", "Macarrão", 8),
            ("30/05/2025", "Carne", 20),
            ("30/05/2025", "Frango", 15),
            ("30/05/2025", "Leite", 12),
            ("30/05/2025", "Ovos", 30),
            ("30/05/2025", "Pão", 25),
            ("30/05/2025", "Manteiga", 18),
            ("30/05/2025", "Queijo", 22),
            ("30/05/2025", "Maçã", 40),
            ("30/05/2025", "Banana", 35),
            ("30/05/2025", "Laranja", 28),
            ("30/05/2025", "Tomate", 15),
            ("30/05/2025", "Cenoura", 10),
            ("30/05/2025", "Batata", 20),
            ("30/05/2025", "Cebola", 18),
            ("30/05/2025", "Alho", 12),
            ("30/05/2025", "Brócolis", 8),
            ("30/05/2025", "Espinafre", 6),
            ("30/05/2025", "Pepino", 14),
            ("30/05/2025", "Abobrinha", 10),
            ("30/05/2025", "Berinjela", 9),
            ("30/05/2025", "Pimentão", 11),
            ("30/05/2025", "Alface", 7),
            ("30/05/2025", "Repolho", 13),
            ("30/05/2025", "Rúcula", 5),
            ("30/05/2025", "Salsa", 4)
        ]

        scrollbar = ttk.Scrollbar(self, orient="vertical")
        table = ttk.Treeview(self, columns=("data", "produto", "quantidade"), show="headings", yscrollcommand=scrollbar.set)
        
        table.heading("data", text="Data")
        table.heading("produto", text="Produto")
        table.heading("quantidade", text="Quantidade")

        table.column("data", anchor="center")
        table.column("produto", anchor="center")
        table.column("quantidade", anchor="center")

        for register in data:
            table.insert("", "end", values=register)

        table.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
