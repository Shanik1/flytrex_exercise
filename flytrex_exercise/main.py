import pandas
import os
from zipfile import ZipFile


def get_data():
    with ZipFile(os.path.join(os.path.dirname(__file__), 'resources', 'weather_data.csv.zip'), 'r') as zip_file:
        with zip_file.open('weather_data.csv') as csv_file:
            df = pandas.read_csv(csv_file)
    return df


def main():
    df = get_data()
    

if __name__ == '__main__':
    main()
