class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.name}, Email: {self.email}"


class UserManager:
    def __init__(self):
        self.users = []

    # Create
    def add_user(self, user_id, name, email):
        user = User(user_id, name, email)
        self.users.append(user)
        print("User added successfully.")

    # Read
    def view_users(self):
        if not self.users:
            print("No users found.")
        for user in self.users:
            print(user)

    # Update
    def update_user(self, user_id, new_name, new_email):
        for user in self.users:
            if user.user_id == user_id:
                user.name = new_name
                user.email = new_email
                print("User updated successfully.")
                return # return here is used to stop the function
        print(" User not found.")
    # Delete
    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print("🗑️ User deleted successfully.")
                return
        print("User not found.")


# Sample usage
manager = UserManager()

# Create
manager.add_user(1, "Alice", "alice@example.com")
manager.add_user(2, "Bob", "bob@example.com")

# Read
manager.view_users()

# Update
manager.update_user(1, "Alice Smith", "alice.smith@example.com")

# Delete
manager.delete_user(2)

# View after changes
manager.view_users()
