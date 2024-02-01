#!/usr/bin/python3
"""A script that:
- takes in a URL, email
- sends a POST request to the passed URL with the email as a parameter
- displays the body of the response
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    res = requests.post(url, data=value)
    print(res.text)
