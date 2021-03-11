# !/usr/bin/python

import os
import requests
import re
import json

list_url = "https://pixeldrain.com/api/list"
id_ending = ".pixel"

list_payload = {
    "title": "test",
    "anonymous": True,
    "files": [
        #    {"id": "abc123", "description": "First photo of the week, such a beautiful valley"},
    ]
}

for root, dirs, files in os.walk("."):
    for name in files:
        path = os.path.join(root, name)
        if not name.endswith(id_ending):
            continue

        with open(path, 'r') as file:
            data = file.read()
        list_payload["files"].append({"id":data})

print(json.dumps(list_payload))
r = requests.post(list_url, json=list_payload)
print(r.text)
