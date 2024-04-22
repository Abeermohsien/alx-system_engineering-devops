#!/usr/bin/python3
"""apu export"""
import csv
import requests
import sys

if __name__ == '__main__':
    usr = sys.argv[1]
    url_usr = 'https://jsonplaceholder.typicode.com/users/' + usr
    res = requests.get(url_usr)
    """get url"""
    usr_name = res.json().get('username')
    task = url_usr + '/todos'
    res = requests.get(task)
    tasks = res.json()

    with open('{}.csv'.format(usr), 'w') as csvfile:
        for task in tasks:
            completed = task.get('completed')
            """completed"""
            title_task = task.get('title')
            """end"""
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                usr, usr_name, completed, title_task))
