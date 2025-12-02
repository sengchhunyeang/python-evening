import json
import os

F = "users.json"

# Load users
if os.path.exists(F):
    with open(F) as f:
        users = json.load(f)
else:
    users = []

# Signup
def signup():
    u = input("Username: ")
    for user in users:
        if user["u"] == u:
            print("Exists!")
            return
    p = input("Password: ")
    users.append({"u": u, "p": p})
    with open(F, "w") as f:
        json.dump(users, f)
    print("Signed up!")

# Login
def login():
    u = input("Username: ")
    p = input("Password: ")
    for user in users:
        if user["u"] == u and user["p"] == p:
            print("Logged in!")
            return
    print("Wrong!")

# Main
while True:
    c = input("1.Signup 2.Login 3.Exit: ")
    if c == "1":
        signup()
    elif c == "2":
        login()
    elif c == "3":
        break
