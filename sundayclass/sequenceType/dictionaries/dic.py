#what is dictionaries ?
mycar ={
    "brand":"Toyota",
    "model":"Camary",
    "year":1999
}

print(mycar)
print(mycar["brand"])
print(mycar["year"])

x = mycar.get("brand")
print("Using get function ",x)
y = mycar.get("year")
print("Using get function ",y)