import json

#
json_text = '{"name": "Andy", "age": 23, "hobbies": ["tennis", "basketball"]}'

jsonToPy = json.loads(json_text)
print(jsonToPy)
print(type(jsonToPy))

print(jsonToPy['age'])


