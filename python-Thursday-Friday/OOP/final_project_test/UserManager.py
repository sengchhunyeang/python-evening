from user import *


class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user_id, user_name, user_email):
        user = User(user_id, user_name, user_email)
        self.users.append(user)
        print("User added successfully!")

    def view_user(self):
        if not self.users:
            print("No users found.")
        else:
            for user in self.users:
                print(user)

    def update_user(self, user_id, new_name=None, new_email=None):
        for user in self.users:
            if user.user_id == user_id:
                if new_name:
                    user.user_name = new_name
                if new_email:
                    user.user_email = new_email
                    print(f"User with ID {user_id} successfully:")
                    return
                print("User not found.")

    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(f"User with ID {user_id} successfully!")
                return
        print("User not found.")
