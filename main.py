#!/usr/bin/env python3

"""
Module Docstring
"""

__author__ = "Keith Moore"
__version__ = "0.1.0"
__license__ = "MIT"

import sys


def get_data(state):
    import requests
    base_url = "https://covidtracking.com/api/v1/states/" + state + "/daily.json"
    r = requests.get(base_url)
    return r.json()


def write_csv(data, state):
    import csv
    keys = data[0].keys()
    filename = "covid-19-" + state + "-data-python.csv"
    with open(filename, "w", newline="") as outfile:
        dict_writer = csv.DictWriter(outfile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


def main():
    """ Main entry point of the app """
    args = len(sys.argv)
    state = 'ga'
    if args > 1:
        state = sys.argv[1]

    print("state: " + state)

    data = get_data(state)
    # print(data)
    write_csv(data, state)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
