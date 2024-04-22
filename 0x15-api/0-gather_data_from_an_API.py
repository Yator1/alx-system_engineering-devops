#!/usr/bin/python3

"""
A python script that uses REST API.
For a given employee ID, it returns information about their TODO list
"""

import requests
import sys


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com'

    employee_ID = sys.argv[1]
    user_response = requests.get(base_url + "/users/{}".format(employee_ID))
    user = user_response.json()
    params = {"userID": employee_ID}
    todos_response = requests.get(base_url + "/todos", params=params)
    todos = todos_response.json()
    completed = []

    for todo in todos:
        if todo.get("completed") is True:
            completed.append(todo.get("title"))
    print("Employee {} is done with tasks({}/{})".format(user.get("name"),
        len(completed), len(todos)))

    for complete in completed:
        print("\t {}".format(complete))
