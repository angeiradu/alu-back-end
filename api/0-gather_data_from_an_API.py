#!/usr/bin/python3

import sys
import requests


def get_employee_todo_progress(employee_id):
    # Construct the URL for the API request
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)

    # Send a GET request to the API and retrieve the response
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response data as JSON
        todos = response.json()

        # Get the employee name
        employee_name = todos[0]['name']

        # Count the number of completed tasks
        completed_tasks = [todo for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)

        # Calculate the total number of tasks
        total_tasks = len(todos)

        # Display the employee TODO list progress
        print("Employee {} is done with tasks({}/{}):".format(employee_name, num_completed_tasks, total_tasks))
        for task in completed_tasks:
            print("\t{}".format(task['title']))
    else:
        print("Error: Failed to retrieve employee TODO list.")


if __name__ == "__main__":
    # Check if the employee ID was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
    else:
        # Get the employee ID from the command-line argument
        employee_id = int(sys.argv[1])

        # Call the function to get the employee TODO list progress
        get_employee_todo_progress(employee_id)
