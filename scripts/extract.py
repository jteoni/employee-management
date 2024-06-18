import os
import pandas as pd


class Extractor:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.employees_data = self.load_employees_data()

    def load_employees_data(self):
        try:
            data = pd.read_csv(self.data_dir)
            if not isinstance(data, pd.DataFrame):
                raise TypeError(f"Expected a DataFrame @ Extractor")
            return data
        except FileNotFoundError as e:
            print(f"Error loading data: {e}")
            return None
        except pd.errors.EmptyDataError as e:
            print(f"No data: {e}")
            return None
        except pd.errors.ParserError as e:
            print(f"Error parsing data: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
