# try:
#   print(10)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

from module import *

# hadle error
var = "hello try except "
# try:
#     message_one(var)
# except:
#     print(var)
try:
    message_one() 
except:
    message_one()
else:
    print("code no error ")
finally:
    print("Finally program is proccesing")
