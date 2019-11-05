import csv
import pathlib


def path_exists(path):
    path = pathlib.Path(path)
    return path.exists()


def read_csv_file(path, fieldnames = None):
    with open(path, newline='') as file:
        reader = csv.DictReader(file, fieldnames)
        return [r for r in reader]
