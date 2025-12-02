
import bankingRunning
username = input("Username : ")
password = input("Password : ")

if username == "Sompu" and password == "1234":
    print("Login Successful")

    bankingRunning.bankingRunning()
else :
    print("Login failed")


