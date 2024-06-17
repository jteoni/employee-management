import os
import pandas as pd


class Extractor:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        self.employees_data = self.load_employees_data()

    def load_employees_data(self):
        try:
            data = pd.read_csv(self.data_dir)
            return data
        except FileNotFoundError as e:
            print(f"Error loading data: {e}")
            return None
