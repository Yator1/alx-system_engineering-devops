#!/usr/bin/python3

"""
A python script that uses REST API.
For a given employee ID, it returns information about their TODO list
Adding line in order to export data in CSV format
Improving the code to export the data in json format
"""

import requests
import sys
import csv
import json


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

        # Creating the csv file for export
        csv_file = f"{employee_id}.csv"
        with open(csv_file, mode='w', newline='') as file:
            csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in todo_data:
                csv_writer.writerow([
                    (employee_id),
                    (employee_name),
                    (task["completed"]),
                    (task["title"])
                    ])

        # Creating a dictionary to store data and export it in json format
        tasks_dict = {employee_id: [{
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
            } for task in todo_data]
        }

        # export the data in json format
        json_file = f"{employee_id}.json"
        with open(json_file, mode='w') as json_file_write:
            json.dump(tasks_dict, json_file_write)


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
