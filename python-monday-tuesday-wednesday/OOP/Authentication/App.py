# app.py
from UserDatabase import UserDatabaseStore
from UserRegister import UserRegister
from UserLogin import UserLogin

class App:
    def __init__(self):
        self.database = UserDatabaseStore()
        self.login_handler = UserLogin(self.database)

    def register(self, first_name, last_name, email, password):
        user = UserRegister(first_name, last_name, email, password)
        self.database.add_user(user)

    def login(self, email, password):
        return self.login_handler.authenticate(email, password)


# ==== Example Run ====
if __name__ == "__main__":
    app = App()

    # Register users
    app.register("John", "Doe", "john@example.com", "1234")
    app.register("Jane", "Smith", "jane@example.com", "abcd")

    # Try login
    app.login("john@example.com", "1234")
    app.login("jane@example.com", "wrong")
