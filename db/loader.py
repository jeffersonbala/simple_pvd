import pandas as pd

class Loader:

    @staticmethod
    def file_loader(path):
        match path.split('.')[-1]:
            case 'csv':
                return pd.read_csv
            case 'json':
                return pd.read_json
            case 'xlsx':
                return pd.read_excel
            case _:
                raise ValueError("Unsupported file type")