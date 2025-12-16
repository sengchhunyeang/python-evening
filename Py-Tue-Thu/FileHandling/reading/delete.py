import os
if os.path.exists("python.txt"):
    os.remove("python.txt")
else:
    with open("python.txt","w") as f :
        f.write("Something")
