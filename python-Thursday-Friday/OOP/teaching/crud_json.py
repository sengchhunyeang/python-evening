import json

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email
        }

    @staticmethod
    def from_dict(data):
        return User(data['user_id'], data['name'], data['email'])

    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.name}, Email: {self.email}"


class UserManager:
    def __init__(self, filename='users.json'):
        self.filename = filename
        self.users = []
        self.load_users()

    def add_user(self, user_id, name, email):
        self.users.append(User(user_id, name, email))
        self.save_users()
        print("✅ User added.")

    def view_users(self):
        if not self.users:
            print("⚠️ No users found.")
        for user in self.users:
            print(user)

    def update_user(self, user_id, new_name, new_email):
        for user in self.users:
            if user.user_id == user_id:
                user.name = new_name
                user.email = new_email
                self.save_users()
                print("✅ User updated.")
                return
        print("❌ User not found.")

    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                self.save_users()
                print("🗑️ User deleted.")
                return
        print("❌ User not found.")

    def save_users(self):
        with open(self.filename, 'w') as f:
            json.dump([user.to_dict() for user in self.users], f, indent=4)

    def load_users(self):
        try:
            with open(self.filename, 'r') as f:
                users_data = json.load(f)
                self.users = [User.from_dict(u) for u in users_data]
        except FileNotFoundError:
            self.users = []
# # Sample usage
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