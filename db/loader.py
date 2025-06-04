import pandas as pd

__BASE_PATH = "data/"

__BASE_CLIENTS_PATH = f"{__BASE_PATH}clients.csv"
__BASE_SALES_PATH = f"{__BASE_PATH}sales.csv"
__BASE_PRODUCTS_PATH = f"{__BASE_PATH}stock.csv"

class Loader:

    @staticmethod
    def file_loader(path):
        match path.split('.')[-1]:
            case 'csv':
                return pd.read_csv(path)
            case 'json':
                return pd.read_json(path)
            case 'xlsx':
                return pd.read_excel(path)
            case _:
                raise ValueError("Unsupported file type")
            
    @staticmethod
    def update_file(data: pd.DataFrame, filename):
        try:
            data.to_csv(f"{filename}.csv", index=False)
            data.to_json(f"{filename}.json", orient='records')
        except Exception as e:
            return f"Error saving file: {e}"
        return f"File {filename} updated successfully in all formats."
    


    