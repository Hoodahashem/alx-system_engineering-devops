#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':

    if len(sys.argv) > 1:
        id = sys.argv[1]
        request = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}").json()
        employee_name = request.get("name")

        another_one = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}/todos").json()
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


        print("Employee {} is done with tasks({}/{}):".format(employee_name, true_count, total))
        for x in task_title:
            print("\t {}".format(x))
