from faker import Faker
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '/')))

fake = Faker()
num_employees = 100

data = {
    'Name': [fake.name() for _ in range(num_employees)],
    'Job': [fake.job() for _ in range(num_employees)],
    'Departament': [fake.random_element(elements=('Sales', 'MKT', 'IT', 'Financial')) for _ in range(num_employees)],
    'Start_date': [fake.date_between(start_date='-5y', end_date='today') for _ in range(num_employees)],
    'Salary': [fake.random_int(min=3000, max=20000) for _ in range(num_employees)],
    'Email': [fake.email() for _ in range(num_employees)],
    'Phone': [fake.phone_number() for _ in range(num_employees)],
    'Address': [fake.address() for _ in range(num_employees)],
    'Age': [fake.random_int(min=18, max=65) for _ in range(num_employees)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame in CSV file
output_file = os.path.join('data', 'employees.csv')
df.to_csv(output_file, index=False)

print(f'Data generated and saved at {output_file}')
