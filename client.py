import json
import pprint
import requests


with open('calls.json', 'r') as f:

    response = requests.post('http://127.0.0.1:5000/fn', json=json.load(f))

if response.ok:

    pprint.pprint(response.json())
