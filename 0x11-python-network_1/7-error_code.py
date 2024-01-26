#!/usr/bin/python3
"""
    a Python script that takes in a URL, sends a request to the URL
    and displays the body of the response.
"""
import requests
from sys import argv

if __name__ == '__main__':
    r = requests.get(argv[1])
    status = r.status_code
    if status < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
