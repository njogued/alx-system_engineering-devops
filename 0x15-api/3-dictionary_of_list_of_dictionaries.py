#!/usr/bin/python3
"""Save all user tasks in a json file"""

import json
from requests import get


if __name__ == "__main__":
    usrs = get(f"https://jsonplaceholder.typicode.com/users/").json()
    ids = {}
    for user in usrs:
        ids[user["id"]] = user["username"]
    todos = get("https://jsonplaceholder.typicode.com/todos").json()
    file_name = "todo_all_employees.json"
    json_dict = {}
    for user_id in ids.keys():
        all_tasks = []
        for tasks in todos:
            if tasks["userId"] == user_id:
                tasks_dict = {}
                tasks_dict["username"] = ids[user_id]
                tasks_dict["task"] = tasks["title"]
                tasks_dict["completed"] = tasks["completed"]
                all_tasks.append(tasks_dict)
                json_dict[str(user_id)] = all_tasks

    with open(file_name, 'w') as f:
        json.dump(json_dict, f)
