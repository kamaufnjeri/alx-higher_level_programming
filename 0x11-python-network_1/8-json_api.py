#!/usr/bin/python3
"""Using requests module"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    data = {}
    if sys.argv[1]:
        data['q'] = sys.argv[1]
    else:
        data['q'] = ""
    try:
        request = requests.post(url, data=data)
        d_json = request.json()

        if d_json == {}:
            print("No result")
        else:
            print(f"[{d_json.get('id')}] {d_json.get('name')}")

    except ValueError:
        print("Not a valid JSOS")    
