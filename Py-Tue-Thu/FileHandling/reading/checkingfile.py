# for checking file
import os # module operation on your Os Operating System Window MacOs Linux Android KromaOs
# if os.path.exists("pythons.png"):
#     print("python Exist")
# else :
#     print("Not found ")


if os.path.exists("doc.txt"):
    os.remove("doc.txt")
    print("Successfully removed doc.txt")
else:
    with open("doc.txt","w") as f:
        f.write("File Handling ")
        print("Successfully added doc.txt")

