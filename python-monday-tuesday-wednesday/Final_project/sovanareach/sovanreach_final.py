class User:
    def __init__(self,user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def str(self):
        return f"ID: {self.user_id}, Name: {self.name}, Email: {self.email}"


class UserManager:
    def __init__(self):
        self.users = []

    # Create
    def add_user(self, user_id, name, email):
        #for user in self.users:
        #    if user.user_id == user_id:
          #      print("User ID already exists!")
           #     return
        #new_user = User(user_id, name, email)
        self.users.append(User(user_id, name, email))
        print("User added successfully!")

    # Read
    def view_users(self):
        if not self.users:
            print("No users found.")
        else:
            print("\n--- User List ---")
            for user in self.users:
                print(user.user_id,user.name,user.email)

    # Update
    def update_user(self, user_id, new_name, new_email):
        for user in self.users:
            if user.user_id == user_id:
                user.name = new_name
                user.email = new_email
                print("User updated successfully!")
                return
        print("User ID not found!")

    # Delete
    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print("User deleted successfully!")
                return
        print("User ID not found!")


def menu():
    manager = UserManager()
    manager.add_user("1", "Alice", "Alice@gmail.com")
    while True:
        print("========== User Management System ==========")
        print("1 - Add User")
        print("2 - View Users")
        print("3 - Update User")
        print("4 - Delete User")
        print("5 - Exit")

        choice = input("Enter your number (1-5): ")

        if choice == "1":
            uid = input("Enter User ID: ")
            name = input("Enter User Name: ")
            email = input("Enter User Email: ")
            manager = UserManager()
            manager.add_user(uid, name, email)

        elif choice == "2":
            manager.view_users()

        elif choice == "3":
            uid = input("Enter User ID to update: ")
            name = input("Enter New Name: ")
            email = input("Enter New Email: ")
            manager.update_user(uid, name, email)

        elif choice == "4":
            uid = input("Enter User ID to delete: ")
            manager.delete_user(uid)

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


#if name == "mainpythonproject":
menu()