from tkinter import ttk
from .base import BaseView

class ClientView(BaseView):

    def __init__(self, parent=None):
        super().__init__()

        self.parent = parent

        self.create_widgets()

        self.visible = True

    def create_widgets(self):
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        icon_label = ttk.Label(self, text="👤 Clientes", font=("Source Code Mono", 64))
        icon_label.grid(row=0, column=0, columnspan=3, pady=20)

        title_label = ttk.Label(self, text="Gerenciamento de Clientes", font=("Source Code Mono", 32))
        title_label.grid(row=1, column=0, columnspan=3, pady=20)

        add_client_button = ttk.Button(self, text="Adicionar Cliente")
        add_client_button.grid(row=2, column=0, padx=10, pady=10)

        edit_client_button = ttk.Button(self, text="Editar Cliente")
        edit_client_button.grid(row=2, column=1, padx=10, pady=10)

        close_button = ttk.Button(self, text="Fechar", command=self.destroy)
        close_button.grid(row=2, column=2, padx=10, pady=10)

        self.create_table([])

    def create_table(self, data):
        
        data = [
            ("01/01/2025", "João Silva", "12345678901", "Ativo"),
            ("15/02/2025", "Maria Oliveira", "98765432100", "Inativo"),
            ("30/03/2025", "Pedro Santos", "45678912300", "Ativo"),
        ]

        columns = ("Data de Cadastro", "Nome", "CPF", "Status")

        scrollbar = ttk.Scrollbar(self, orient="vertical")
        table = ttk.Treeview(self, columns=columns, show='headings', yscrollcommand=scrollbar.set)

        table.heading("Data de Cadastro", text="Data de Cadastro")
        table.heading("Nome", text="Nome")
        table.heading("CPF", text="CPF")
        table.heading("Status", text="Status")

        table.column("Data de Cadastro", width=120)
        table.column("Nome", width=200)
        table.column("CPF", width=120)
        table.column("Status", width=100)

        for row in data:
            table.insert("", "end", values=row)
        table.grid(row=3, column=0, columnspan=3, sticky="nsew")

        scrollbar.config(command=table.yview)
        scrollbar.grid(row=3, column=3, sticky="ns")

    def get_add_client_button(self):
        return self.grid_slaves(row=2, column=0)[0]
    
    def get_edit_client_button(self):
        return self.grid_slaves(row=2, column=1)[0]
    
    
