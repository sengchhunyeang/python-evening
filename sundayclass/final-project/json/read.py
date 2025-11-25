# How to read json data python
# import json
#
# with open("data.json", "r") as file:
#     data = json.load(file)
#
# print(data)


import json

with open("data.json", "r") as file:
    # for convert json to dictionary
    information = json.load(file)
    print(type(information))
    print(information)
