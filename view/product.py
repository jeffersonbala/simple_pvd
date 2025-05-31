from .base import BaseView
from tkinter import ttk

class ProductView(BaseView):

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

        icon_label = ttk.Label(self, text="🛍️ Produtos", font=("Source Code Mono", 64))
        icon_label.grid(row=0, column=0, columnspan=3, pady=20)

        new_product_button = ttk.Button(self, text="Novo Produto")
        new_product_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        back_button = ttk.Button(self, text="Fechar", command=self.destroy)
        back_button.grid(row=2, column=2, padx=10, pady=10)

        self.create_table()

    def get_close_button(self):
        return self.grid_slaves(row=2, column=2)[0]
    
    def get_new_product_button(self):
        return self.grid_slaves(row=2, column=0)[0]
    
    def create_table(self):
        # TODO: Get products from stock database

        data = [
            ("Arroz", 10, "R$ 5,00"),
            ("Feijão", 5, "R$ 4,00"),
            ("Macarrão", 8, "R$ 3,00"),
            ("Carne", 20, "R$ 15,00"),
            ("Frango", 15, "R$ 10,00"),
            ("Leite", 12, "R$ 2,50"),
            ("Ovos", 30, "R$ 0,50"),
            ("Pão", 25, "R$ 1,00"),
            ("Manteiga", 18, "R$ 3,50"),
            ("Queijo", 22, "R$ 6,00"),
            ("Maçã", 40, "R$ 1,20"),
            ("Banana", 35, "R$ 0,80"),
            ("Laranja", 28, "R$ 1,50")
        ]

        scrollbar = ttk.Scrollbar(self, orient="vertical")
        table = ttk.Treeview(self, columns=("Descrição", "Quantidade", "Preço"), show="headings", yscrollcommand=scrollbar.set)

        table.heading("Descrição", text="Descrição")
        table.heading("Quantidade", text="Quantidade")
        table.heading("Preço", text="Preço")

        table.column("Descrição", width=200)
        table.column("Quantidade", width=100)
        table.column("Preço", width=100)

        for item in data:
            table.insert("", "end", values=item)

        table.grid(row=1, column=0, columnspan=3, sticky="nsew")