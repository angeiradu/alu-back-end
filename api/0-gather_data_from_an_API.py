#!/usr/bin/python3
"""script that fetches info about a given employee's ID using an api"""
import json
import requests
import sys

base_url = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 script_name.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]

    # get user info e.g https://jsonplaceholder.typicode.com/users/1/
    user_url = '{}/users?id={}'.format(base_url, user_id)

    # get info from api
    response = requests.get(user_url)

    if response.status_code != 200:
        print("Error: Failed to fetch user information.")
        sys.exit(1)

    # pull data from api
    data = response.json()

    if not data:
        print("Error: No employee found with the provided ID.")
        sys.exit(1)

    # extract user data, in this case, name of employee
    name = data[0].get('name')

    # get user info about todo tasks
    # e.g https://jsonplaceholder.typicode.com/users/1/todos
    tasks_url = '{}/todos?userId={}'.format(base_url, user_id)

    # get info from api
    response = requests.get(tasks_url)

    if response.status_code != 200:
        print("Error: Failed to fetch tasks information.")
        sys.exit(1)

    # pull data from api
    tasks = response.json()

    # initialize completed count as 0 and find total number of tasks
    completed = 0
    total_tasks = len(tasks)

    # initialize empty list for completed tasks
    completed_tasks = []
    # loop through tasks counting number of completed tasks
    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            completed += 1

    # print the output in the required format
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
