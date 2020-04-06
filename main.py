#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Keith Moore"
__version__ = "0.1.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    data = get_data()
    calculate_daily_new_cases(data)
    print(data)
    write_csv(data)


def get_data():
    from datetime import datetime, timedelta
    import requests
    data = []
    base_url = "https://covidtracking.com/api/states/daily?state=GA&date="
    today = datetime.today()
    formatted_date = today.strftime("%Y%m%d")
    while formatted_date != "20200315":
        print(formatted_date)
        r = requests.get(base_url + formatted_date)
        d = r.json()
        if isinstance(d, list) == False and 'error' not in d:
            data.append(d)
        today = today - timedelta(days=1)
        formatted_date = today.strftime("%Y%m%d")
    return data


def calculate_daily_new_cases(data):
    length = len(data)
    for idx, obj in enumerate(data):
        if idx < (length - 1):
            prev = data[idx + 1]
            if 'positive' in prev and 'positive' in obj:
                diff = obj['positive'] - prev['positive']
                obj['newCases'] = diff
        else:
            obj['newCases'] = None


def write_csv(data):
    import csv
    keys = data[0].keys()
    with open("covid-19-ga-data-python.csv", "w", newline="") as outfile:
        dict_writer = csv.DictWriter(outfile, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
