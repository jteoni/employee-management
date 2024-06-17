import pandas as pd


class Transformer:
    def __init__(self, employees_data):
        self.employees_data = employees_data

    def calculate_average_age(self):
        try:
            df = self.employees_data.copy()
            df['age'] = df['age'].dt.age
            average_age = df['age'].mean()
            return average_age
        except Exception as e:
            print(f"Error calculating average age: {e}")
            raise

    def process_data(self):
        try:
            average_age = self.calculate_average_age()

            expected_columns = ['Name', 'Job', 'Departament', 'Start_date', 'Salary', 'Email', 'Phone', 'Address',
                                'Age']
            transformed_data = pd.Series(average_age, index=expected_columns)
            return transformed_data
        except Exception as e:
            print(f"Error processing data: {e}")
            raise
