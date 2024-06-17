import pandas as pd
import os
from pathlib import Path
from scripts.extract import Extractor
from scripts.load import Loader
from scripts.transform import Transformer

input_file = os.path.join('data', 'employees.csv')
df = pd.read_csv(input_file)


def main():
    data_dir = "data/"
    output_dir = "output/"

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    extractor = Extractor(input_file)
    employees_data = extractor.load_employees_data()

    transformer = Transformer(employees_data)
    transformed_data = transformer.process_data()

    loader = Loader(output_dir)
    loader.save_data(transformed_data, filename='output.csv')


if __name__ == '__main__':
    # Execute the main function if the script is run directly
    main()
