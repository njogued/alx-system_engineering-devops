#!/usr/bin/python3
"""Save the tasks in a CSV file"""

import csv
from requests import get
from sys import argv as v

if __name__ == "__main__":
    usr = v[1]
    usrs = get(f"https://jsonplaceholder.typicode.com/users/{usr}").json()
    todos = get("https://jsonplaceholder.typicode.com/todos").json()
    username = usrs["username"]
    all_tasks = []
    file_name = f"{usr}.csv"

    for tasks in todos:
        if tasks["userId"] == int(usr):
            status = tasks["completed"]
            task = tasks["title"]
            full = f'"{usr}","{username}","{status}","{task}"\n'
            all_tasks.append(full)

    with open(file_name, 'w') as f:
        for usr_task in all_tasks:
            f.write(usr_task)
            
