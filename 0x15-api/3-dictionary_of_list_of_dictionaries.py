#!/usr/bin/python3
"""api"""

import json
import requests
import sys


if __name__ == '__main__':
    URL = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(URL)
    Users = res.json()

    user_dict = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        URL = 'https://jsonplaceholder.typicode.com/users/{}'.format(USER_ID)
        URL = URL + '/todos/'
        res = requests.get(URL)

        tasks = res.json()
        user_dict[USER_ID] = []
        for task in tasks:
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            user_dict[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
            """documentation"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_dict, f)
