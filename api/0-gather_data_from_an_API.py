#!/usr/bin/python3
"""
Gathers data from an API and displays the TODO list progress for a given employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 gather_data.py employee_id")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Make a GET request to retrieve employee information
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee = response.json()

    # Make a GET request to retrieve the employee's TODO list
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url)
    todos = response.json()

    # Filter completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]

    # Display the progress
    employee_name = employee['name']
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")
