#!/usr/bin/python3
"""importing requests and sys module"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) > 1:
        user = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        req = requests.get("{}users/{}".format(url, user))
        name = req.json().get("name")
        if name is not None:
            json = requests.get(
                "{}todos?userId={}".format(
                    url, user)).json()
            all_tasks = len(json)
            comp_tasks = []
            for t in json:
                if t.get("completed") is True:
                    comp_tasks.append(t)
            count = len(comp_tasks)
            print("Employee {} is done with tasks({}/{}):"
                  .format(name, count, all_tasks))
            for title in comp_tasks:
                print("\t {}".format(title.get("title")))
