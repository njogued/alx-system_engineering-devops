#!/usr/bin/python3
"""
Save the tasks in a CSV file
"""


import csv
from requests import get
from sys import argv as v


if __name__ == "__main__":
    """
    csv file - Comma Separated Values
    """
    usr = v[1]
    usrs = get("https://jsonplaceholder.typicode.com/users/{}".format(usr))
    usrs = usrs.json()
    todos = get("https://jsonplaceholder.typicode.com/todos").json()
    username = usrs["username"]
    all_tasks = []
    file_name = "{}.csv".format(usr)

    for tasks in todos:
        if tasks["userId"] == int(usr):
            status = tasks["completed"]
            task = tasks["title"]
            full = '"{}","{}","{}","{}"\n'.format(usr, username, status, task)
            all_tasks.append(full)

    with open(file_name, 'w') as f:
        for usr_task in all_tasks:
            f.write(usr_task)
