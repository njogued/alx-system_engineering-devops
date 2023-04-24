#!/usr/bin/python3
"""Save the tasks in a json file"""

import json
from requests import get
from sys import argv as v

if __name__ == "__main__":
    usr = v[1]
    usrs = get(f"https://jsonplaceholder.typicode.com/users/{usr}").json()
    todos = get("https://jsonplaceholder.typicode.com/todos").json()
    username = usrs["username"]
    all_tasks = []
    file_name = f"{usr}.json"

    for tasks in todos:
        if tasks["userId"] == int(usr):
            status = tasks["completed"]
            task = tasks["title"]
            tasks_dict = {}
            tasks_dict["task"] = task
            tasks_dict["completed"] = status
            tasks_dict["username"] = username
            all_tasks.append(tasks_dict)

    with open(file_name, 'w') as f:
        json_dict = {}
        json_dict[usr] = all_tasks
        json.dump(json_dict, f)
            
