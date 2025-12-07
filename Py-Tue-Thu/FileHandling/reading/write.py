# with open("doc.txt","w") as file :
#     file.write("I am instructor \n I am a student at ICT\nI love IT  ")
#
# with open("doc.txt","r") as file :
#     print(file.read())

# can not override
# with open("doc.txt","x") as text :
#     text.write("testing doc.txt \n Hello world ")

with open("python.png","rb") as image :
    file = image.read()
    print(file.__bytes__())