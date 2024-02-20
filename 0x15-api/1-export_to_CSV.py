#!/usr/bin/python3
"""importing requests and sys module"""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        id = sys.argv[1]
        request = requests.get("""
                               https://jsonplaceholder.typicode.com/users/{}\
""".format(id)).json()
        employee_name = request.get("username")

        another_one = requests.get("""
                                   https://jsonplaceholder.typicode.com/users/{}/todos
""".format(id)).json()
        false_count = 0
        true_count = 0
        total = 0
        task_title = []
        for i in another_one:
            if i["completed"] is False:
                false_count += 1
            else:
                true_count += 1
                task_title.append(i["title"])
            total += 1

    with open("{}.csv".format(id), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for x in another_one:
            taskwriter.writerow([int(id), employee_name,
                                x["completed"], x["title"]])
