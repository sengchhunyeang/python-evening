# import json
#
# data = {
#     "name": "Reach ",
#     "age": 24
# }
#
# with open('data.json', 'w') as file:
#     json.dump(data, file, indent=4)

import json
# dictionary
data_information = {
    "name":"Sompu",
    "age":22,
    "hobbies":["Football","Reading","Gaming"]
}
with open("data.json","w") as file:
# for dictionary to json using dump
    json.dump(data_information,file,indent=4)


