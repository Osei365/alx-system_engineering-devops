#!/usr/bin/python3
"""using API to get todo of
customers."""

import requests
import sys


if __name__ == "__main__":
    arg = sys.argv[1]
    home = 'https://jsonplaceholder.typicode.com/'
    r = requests.get('{}todos'.format(home))
    user = requests.get('{}users/{}'.format(home, arg))
    uname = user.json().get('name')
    user_todos = [i for i in r.json() if i.get('userId') == int(arg)]
    done = [task.get('title') for task in user_todos if task.get('completed')]
    print('Employee {} is done with tasks({}/{}):'.format(uname,
                                                          len(done),
                                                          len(user_todos)))
    for i in done:
        print('\t {}'.format(i))
