# for using json:
import json
# dictionary store by key value
information = {
    "name":"Lymeng",
    "age":18
}
# name : key
# value : lymeng

with open("data.json","w") as file :
    # convert dic to json
    # json.dumps()
    data = json.dumps(information,indent=4)
    file.write(data)

# How to reading data json
with open("data.json","r") as file :
    data = json.loads(file.read())
    print("Log type :",type(data))
    print(data)