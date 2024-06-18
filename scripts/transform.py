import pandas as pd


class Transformer:
    def __init__(self, data):
        self.data = data

    def calculate_average_age(self):
        try:
            average_age = self.data['age'].mean()
            print(f"Average age: {average_age}")
            return average_age
        except Exception as e:
            print(f"Error calculating average age: {e}")
            return None

    def process_data(self):
        try:
            self.calculate_average_age()
            return self.data
        except Exception as e:
            print(f"Error processing data: {e}")
        return None
