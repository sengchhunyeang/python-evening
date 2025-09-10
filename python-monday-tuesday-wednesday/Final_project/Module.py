from UserManager import *
# create object from UserManager
user_manager = UserManager() # declare as Global
def user_choose():
    while True:
        print("=" * 20)
        print("1-Add User\n2-View Users\n3-Update User\n4-Delete User\n5-Exit")
        print("=" * 20)
        user_choice = int(input("Enter your choice: "))
        if user_choice == 1:

            user_id = int(input("Enter user ID:"))
            user_name = input("Enter user name:")
            user_email = input("Enter user email:")
            user_manager.add_user(user_id,user_name,user_email)
        elif user_choice == 2:
            print("2-View Users")
            # call view_user() form user_manager
            user_manager.view_users()
        elif user_choice == 3:
            print("3-Update User")
        elif user_choice == 4:
            print("4-Delete User")
        elif user_choice == 5:
            print("System exiting...!")
            exit(0)
