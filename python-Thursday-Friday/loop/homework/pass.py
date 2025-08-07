import time
count = 0
while count < 3 :
    password = input("password: ")
    if password == "hello" :
        print("password is correct ")
    else :
        print("password in correct try again ...")
        print("Waiting 2 seconds before next attempt...")
        time.sleep(2)
    count +=1