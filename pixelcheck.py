# !/usr/bin/python

import os
import requests
import re

file_url = "https://pixeldrain.com/api/file"
id_ending = ".pixel"

for root, dirs, files in os.walk("."):
  for name in files:
    path = os.path.join(root, name)
    if not name.endswith(id_ending):
      continue

    with open(path, 'r') as file:
      data = file.read()
    print("got "+data+" from "+path)
    info_url = file_url + "/" + data + "/info"
    r = requests.get(info_url)
    print(r.text)
    if r.status_code != 200:
        print("would delete "+path)






