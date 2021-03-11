# !/usr/bin/python

import os
import requests
import re

put_url = "https://pixeldrain.com/api/file"
put_regex = r"\"success\":true,\"id\":\"(.*)\""
id_ending = ".pixel"

for root, dirs, files in os.walk("."):
  for name in files:
    path = os.path.join(root, name)
    pixelpath = path + id_ending
    if os.path.exists(pixelpath) or name.endswith(id_ending):
       continue
    print("doing " + path)
    with open(path, 'rb') as f:
      r = requests.post(put_url, files={"file": f})
    matches = re.search(put_regex, r.text)
    id = matches.group(1)
    f = open(path + id_ending, "w")
    f.write(id)
    f.close()
