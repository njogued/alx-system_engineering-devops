#!/usr/bin/python3
"""
Using an api to get json data
Uses the requests module
"""
from requests import get
from sys import argv as v


if __name__ == "__main__":
    # Get user input from command line arguments
    usr = v[1]

    # Generate the URL for the user info based on user input
    usrurl = f"https://jsonplaceholder.typicode.com/users/{usr}"

    # Fetch the todos data from the API and parse it as JSON
    todos = get("https://jsonplaceholder.typicode.com/todos").json()

    # Fetch the user info from the API based on generated URL and parse it as JSON
    usr_info = get(usrurl).json()

    # Extract the user name from the user info
    usr_name = usr_info["name"]

    # Initialize variables for total number of tasks and completed tasks
    total = 0
    completed = 0

    # Initialize an empty list to store titles of completed tasks
    complete_tasks = []

    # Convert user input to integer for comparison with task user id
    usr = int(usr)

    # Loop through each task and update the task counters and task titles list
    for tasks in todos:
        if tasks["userId"] == usr:
            total += 1
        if tasks["userId"] == usr and tasks["completed"] is True:
            completed += 1
            complete_tasks.append(tasks["title"])

    # Print a summary of the completed tasks for the user
    print(f"Employee {usr_name} is done with tasks({completed}/{total}):")
    for task in complete_tasks:
        print(f"\t{task}")
