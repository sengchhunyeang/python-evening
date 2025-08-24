class User:
    def __init__(self,user_id,name,email):
        self.user_id = user_id
        self.name = name
        self.email = email
    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.name}, Email: {self.email}"

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user_id, name, email):
        new_user = User(user_id, name, email)
        self.users.append(new_user)
    print(f"User added success ")

    def view_users(self):
        for user in self.users:
            print(user)
        return

    def update_user(self, user_id, name=None, email=None):
        for user in self.users:
            if user.user_id == user_id:
                if name:
                    user.name = name
                if email:
                    user.email = email
                print(f"User with id {user_id} updated successfully.")
                return
        print(f"User with id {user_id} not found.")

    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
        print(f"user with id {id} deleted successfully.")
        return

    print(f"User with id {id} not found.")

obj = UserManager()
def display_options():
    print(
        f"==============================================================================="
    )
    print("1. ADD USER")
    print("2. VIEW USERS")
    print("3. UPDATE USER")
    print("4. DELETE USER")
    print(
        f"===============================================================================")

def display_menu(choose):
    if choose == "1":
        user_id = input("Enter user id: ")
        name = input("Enter user name: ")
        email = input("Enter user email: ")
        obj.add_user(user_id,name, email)
    elif choose == "2":
        obj.view_users()
    elif choose == "3":
        user_id = input("Enter user id to update: ")
        name = input("Enter new name (leave blank to keep current): ")
        email = input("Enter new email (leave blank to keep current): ")
        obj.update_user(user_id, name, email)
    elif choose == "4":
        user_id = input("Enter user id to delete: ")
        obj.delete_user(user_id)
    else:
        print("Invalid choice. Please try again.")

while True:
    display_options()
    variable = input("Enter your option: ")
    display_menu(variable)
