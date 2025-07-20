# what is dictionary ??
# Dictionaries is store multiple value by key value pair

# how to declare 

# car = {
#     'brand',
#     'color',
#     'Model'
# }
# brand = "Ford"
# color = "Red"
# Model = "ranger"

# fromKey = dict.fromkeys(car,brand)

# print(fromKey)
car = {
    "brand":"ford",
    "color":"Red",
    "Model":"Ranger"
}
valueSetDefault = car.setdefault("color","Blue") #


print(valueSetDefault)
