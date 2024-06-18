from faker import Faker
import pandas as pd
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '/')))

fake = Faker()
num_employees = 100

data = {
    'id': [fake.random_int(min=3000, max=20000) for _ in range(num_employees)],
    'name': [fake.name() for _ in range(num_employees)],
    'job': [fake.random_element(elements=('Teacher', 'Security Guard', 'ADMIN', 'Financial')) for _ in
            range(num_employees)],
    'start_date': [fake.date_between(start_date='-5y', end_date='today') for _ in range(num_employees)],
    'salary': [fake.random_int(min=3000, max=20000) for _ in range(num_employees)],
    'email': [fake.email() for _ in range(num_employees)],
    'phone': [fake.phone_number() for _ in range(num_employees)],
    'address': [fake.address() for _ in range(num_employees)],
    'age': [fake.random_int(min=18, max=65) for _ in range(num_employees)]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame in CSV file
output_file = os.path.join('data', 'employees.csv')
df.to_csv(output_file, index=False)

print(f'Data generated and saved at {output_file}')
