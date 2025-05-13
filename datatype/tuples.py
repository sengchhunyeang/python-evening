# Tuple
# color = ("red","blue","yellow")
# print(color)
# print(color[1])
# # tuples
# # Declare data can not change immutable
# weekday = ("Mon","Tue","Wed","Thu","Fri","Sat","Sun") # using tuples
# # fixed data
# # concatenate Tuple
# color1 = ("orange","cyan")
# allColor = color + color1
# print("color tuples when concat ",allColor)
#
# # find index
# print("index of weekday 2th :",weekday.index("Tue"))

# How to declare Tuple

skin1 = ("black","white","Brown")
skin2 = ("Yellow","Red")
#find index
print(skin1.index("Brown")) # 2
# How to Concat tuples
combine = skin1 + skin2
print("When Combine :",combine)
# what is tuples

# convert to list
new_tuple = list(skin1) # convert tuple to list you need using list()
print("New tuples :",new_tuple)
print("Skin1 Type:",type(skin1))
print("New tuples Type:",type(new_tuple))
