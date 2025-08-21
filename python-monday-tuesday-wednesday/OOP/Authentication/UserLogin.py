from UserDatabase import *


# user_login.py

class UserLogin:
    def __init__(self, database: UserDatabaseStore):
        self.database = database

    def authenticate(self, email, password):
        for user in self.database.get_users():
            if user.email == email and user.password == password:  # FIXED
                print(f"✅ Welcome {user.first_name} {user.last_name}!")
                return True
        print("❌ Invalid email or password.")
        return False

