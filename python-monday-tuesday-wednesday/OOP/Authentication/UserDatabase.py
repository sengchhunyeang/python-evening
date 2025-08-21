# user_database_store.py
from UserRegister import UserRegister

class UserDatabaseStore:
    def __init__(self):
        self.users = []  # list of UserRegister objects

    def add_user(self, user: UserRegister):
        # check if email already exists
        for u in self.users:
            if u.email == user.email:
                print("Email already registered.")
                return False
        self.users.append(user)
        print(f" User {user.first_name} registered successfully.")
        return True

    def get_users(self):
        return self.users
