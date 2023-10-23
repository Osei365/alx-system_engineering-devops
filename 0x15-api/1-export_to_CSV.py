#!/usr/bin/python3
"""using API to get todo of
customers."""

import csv
import requests
import sys


if __name__ == "__main__":
    arg = sys.argv[1]
    filename = '{}.csv'.format(arg)
    home = 'https://jsonplaceholder.typicode.com/'
    user = requests.get('{}users/{}'.format(home, arg))
    uname = user.json().get('username')
    todos = requests.get('{}users/{}/todos'.format(home, arg)).json()
    with open(filename, 'w', newline="") as csvfile:
        csvwriter = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        for t in todos:
            row = ['{}'.format(t.get('userId')),
                   '{}'.format(uname),
                   '{}'.format(t.get('completed')),
                   '{}'.format(t.get('title'))]
            csvwriter.writerow(row)
