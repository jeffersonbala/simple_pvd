class Client:

    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def __repr__(self):
        return f"Client(name={self.name}, address={self.address})"
    
    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address
        }
