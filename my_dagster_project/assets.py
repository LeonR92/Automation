import pandas as pd
from dagster import asset
import os


@asset
def create_dataset():
    # A small fictional dataset as a DataFrame
    data = {
        "name": ["Alice", "Bob", "Charlie"],
        "age": [28, 32, 22],
        "city": ["New York", "Los Angeles", "San Francisco"],
    }
    df = pd.DataFrame(data)
    return df


@asset
def dynamic_dataset_to_csv(create_dataset):
    filename_base = 'dataset'
    extension = '.csv'
    counter = 0
    filename = f"{filename_base}{extension}"

    # Check if the file exists, and if so, increment the counter and generate a new name
    while os.path.exists(filename):
        counter += 1
        filename = f"{filename_base}_{counter}{extension}"

    # Save the DataFrame to the dynamically named CSV file
    create_dataset.to_csv(filename, index=False)
    return f"CSV file saved as '{filename}'"
