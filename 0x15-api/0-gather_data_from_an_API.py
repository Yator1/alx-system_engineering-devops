#!/usr/bin/python3

"""
A python script that uses REST API.
For a given employee ID, it returns information about their TODO list
"""

import requests
import sys


def get_todo(employee_id):
    """
    Returns TODO list for an Employee.
    :param employee_id: The employee's ID.
    """

    base_url = 'https://jsonplaceholder.typicode.com'

    employee_resp = requests.get(f"{base_url}/users/{employee_id}")
    if employee_resp.status_code == 200:
        employee_data = employee_resp.json()
        employee_name = employee_data["name"]
    else:
        return

    todo_resp = requests.get(f"{base_url}/todos?userId={employee_id}")

    if todo_resp.status_code == 200:
        todo_data = todo_resp.json()
    else:
        return

    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task["completed"])

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name,
        completed_tasks,
        total_tasks)
        )

    completed = []
    for task in todo_data:
        if task["completed"]:
            completed.append(task)
    for task in completed:
        print("\t {}".format(task["title"]))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer employee ID")
        sys.exit(1)

    get_todo(employee_id)
