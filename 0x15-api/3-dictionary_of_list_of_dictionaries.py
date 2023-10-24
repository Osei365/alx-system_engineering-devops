#!/usr/bin/python3
"""using API to get todo of
customers."""

import json
import requests


if __name__ == "__main__":
    filename = 'todo_all_employees.json'
    home = 'https://jsonplaceholder.typicode.com/'
    with open(filename, 'w') as f:
        dic = {}
        for i in range(1, 11):
            user = requests.get('{}users/{}'.format(home, i)).json()
            uname = user.get('username')
            user_id = user.get('id')
            todos = requests.get('{}users/{}/todos'.format(home, user_id))
            todos = todos.json()
            row = []
            for t in todos:
                row_dict = {'username': uname,
                            'task': t.get('title'),
                            'completed': t.get('completed')}
                row.append(row_dict)
            dic[user_id] = row
        json.dump(dic, f)
