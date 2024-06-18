import pandas as pd
import os


class Loader:
    def __init__(self, output_path):
        self.output_path = output_path

    def save_data(self, data, filename='output.csv'):
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Expected a DataFrame @ Loader")

        try:
            os.makedirs(self.output_path, exist_ok=True)
            output_file = os.path.join(self.output_path, filename)
            data.to_csv(output_file, index=False)
            print(f"Data saved to {output_file}")
        except Exception as e:
            print(f"Error saving data to CSV: {e}")
            raise

    def get_output_file_path(self, filename):
        return os.path.join(self.output_path, filename)
