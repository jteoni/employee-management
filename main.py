import pandas as pd
import os
from pathlib import Path
from scripts.extract import Extractor
from scripts.load import Loader
from scripts.transform import Transformer


def main():
    data_file = os.path.join('data', 'employees.csv')

    output_dir = "output/"
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    extractor = Extractor(data_file)
    if extractor.employees_data is not None:
        print("Data loaded successfully.")
    else:
        print("Failed to load data.")
        return

    transformer = Transformer(extractor.employees_data)
    transformed_data = transformer.process_data()
    if not isinstance(transformed_data, pd.DataFrame):
        print(f"Expected a DataFrame, but got {type(transformed_data).__name__} instead.")
        return

    loader = Loader(output_dir)
    loader.save_data(transformed_data, filename='output.csv')


if __name__ == '__main__':
    main()
