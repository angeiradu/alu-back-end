#!/usr/bin/python3
import requests

def get_employee_todo_progress(employee_id):
    # Make a GET request to the API endpoint
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        todos = response.json()

        # Filter the completed tasks
        completed_tasks = [todo for todo in todos if todo['completed']]

        # Extract relevant information
        employee_name = todos[0]['name']
        number_of_done_tasks = len(completed_tasks)
        total_number_of_tasks = len(todos)

        # Print the progress information
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_number_of_tasks}):")

        # Print the titles of completed tasks
        for task in completed_tasks:
            print(f"\t{task['title']}")

    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code}")


# Test the function with an employee ID
employee_id = 1
get_employee_todo_progress(employee_id)
