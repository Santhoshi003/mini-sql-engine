import csv
import os

def load_csv(table_name):
    file_path = f"data/{table_name}.csv"

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Table '{table_name}' does not exist")

    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    return data
