#!/usr/bin/env python3

"""
Module Docstring
"""

__author__ = "Keith Moore"
__version__ = "0.1.0"
__license__ = "MIT"


def get_data():
    import requests
    base_url = "https://covidtracking.com/api/v1/states/nc/daily.json"
    r = requests.get(base_url)
    return r.json()


def write_csv(data):
    import csv
    keys = data[0].keys()
    with open("covid-19-nc-data-python.csv", "w", newline="") as outfile:
        dict_writer = csv.DictWriter(outfile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


def main():
    """ Main entry point of the app """
    data = get_data()
    print(data)
    write_csv(data)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
