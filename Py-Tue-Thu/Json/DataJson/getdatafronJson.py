# Reading file
# why learn Json ??
# for basic API
import json

with open("data.json","r") as file:
    # convert json to python
    data = json.loads(file.read())
    print(data)