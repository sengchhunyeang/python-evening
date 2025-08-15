# function 1 no parameter and no return

def menu():
    print("1-add user\n2-update user\n3-delete user\n4-exit")

# function 2 has parameter and no return
def option(opt):
        if opt == "1":
            print("add user")
        elif opt == "2":
            print("update user ")
        elif opt == "3":
            print("delete user ")
        elif opt == "4":
            print("program exit !")
            exit(0)
        else:
            print("please try again")
