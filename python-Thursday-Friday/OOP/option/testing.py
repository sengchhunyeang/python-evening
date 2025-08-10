def display_menu():
    print("=================System Manage User =================")
    print("1-Add User ")
    print("2-View User ")
    print("3-Update User")
    print("4-Delete User")
    print("5-Exit")
    print("=================System Manage User =================")

def input_option(option):
    if option == "1":
        print("1-Add User")
    elif option == "2":
        print("2-View User")
    elif option == "3":
        print("3-Update User")
    elif option == "4":
        print("4-Delete User")
    elif option == "5":
        print("Program exiting...")
        exit(0)
    else:
        print("Something Wrong option ..!")
display_menu()
while True:
    input_opt = input("Choose one  option do you want : ")
    input_option(input_opt)
    display_menu()