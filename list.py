from operator import index
# List is container stored data. that we can call that data by index.
# 1 list is container stored data

# 2 How to declare

# myList = ["A","B","C","D"]


# color= ["red","blue","green",13] # Declare
# #index : 0,1,2,3........
# print("are my list :",color) # call
# print("Print index :",color[3])
# print("Print index :",color[1])
#
# day = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
#
# print("day of weeks",day)
# print("Today is ",day[1]) # call by index
#
#
# print("find index Sunday :",day.index("Sunday"))

# myAnimal= ["Cat","Dog","Cow","Tiger"]
# print("These are myAnimal:",myAnimal) # Print list
# print("This is :",myAnimal[2]) # Print by index
# print("Finding Index of Tiger :",myAnimal.index("Tiger")) # find index of items
#
# # How to delete dog from myAnimal ?
# # 1 Modify list
# myAnimal[1] = "Duck"
#
# print("This are New myAnimal:",myAnimal)
# myAnimal[3] = "Dog"
#
# print("This are New2 myAnimal:",myAnimal)

color = ["Black","yellow","green"]
print("list 1",color)
color.remove("yellow") # using remove() for delete item from list
print("List 2 ",color)

# How to delete items by index ?
color.pop(1) # using pop() for remove items from list by index
print("List 3 ",color)

# remove() vs pop() what are difference?


# Homework
# 1 create list
# 2 modify list
# 3 remove list using remove()
# 4 remove list by index using pop()
myStudent = [""]