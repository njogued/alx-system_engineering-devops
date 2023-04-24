#!/usr/bin/python3
"""Using an api to get json data"""

from sys import argv as v
from requests import get

if __name__ == "__main__":
    usr = v[1]
    usrurl = f"https://jsonplaceholder.typicode.com/users/{usr}"
    todos = get("https://jsonplaceholder.typicode.com/todos").json()
    usr_info = get(usrurl).json()
    usr_name = usr_info["name"]
    total = 0
    completed = 0
    complete_tasks = []
    usr = int(usr)
    for tasks in todos:
        if tasks["userId"] == usr:
            total += 1
        if tasks["userId"] == usr and tasks["completed"] == True:
            completed += 1
            complete_tasks.append(tasks["title"])

    print(f"Employee {usr_name} is done with tasks({completed}/{total}):")
    for task in complete_tasks:
        print(f"\t{task}")
