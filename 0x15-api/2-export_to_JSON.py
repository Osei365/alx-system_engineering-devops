#!/usr/bin/python3
"""using API to get todo of
customers."""

import json
import requests
import sys


if __name__ == "__main__":
    arg = sys.argv[1]
    filename = '{}.json'.format(arg)
    home = 'https://jsonplaceholder.typicode.com/'
    user = requests.get('{}users/{}'.format(home, arg)).json()
    uname = user.get('username')
    todos = requests.get('{}users/{}/todos'.format(home, arg)).json()
    with open(filename, 'w') as f:
        dic = {}
        row = []
        for t in todos:
            row_dict = {'task': t.get('title'),
                        'completed': t.get('completed'),
                        'username': uname}
            row.append(row_dict)
        dic[t.get('userId')] = row
        json.dump(dic, f)
