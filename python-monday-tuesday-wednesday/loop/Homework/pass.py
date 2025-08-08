
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
END = "\033[0m"
import time
username = "chhunyeang"
password_set = "ICT@123"
countInput = 0
while countInput < 3 :
     password = input("password :")
     if password == password_set :
         print(f"{GREEN}PASSWORD IS CORRECT {END}")
         break 
     else : 
        print(f"{RED}Password incorrect \n try again {END} ")
        print("Waiting for 2 second ")
        time.sleep(2)
     countInput +=1