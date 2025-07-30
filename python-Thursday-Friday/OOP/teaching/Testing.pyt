from colorama import init, Fore, Style

init(autoreset=True)

# ----- User Class -----
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"ID: {self.user_id}, Name: {self.name}, Email: {self.email}"

# ----- UserManager Class -----
class UserManager:
    def __init__(self):
        self.users = []
        self.next_id = 1  # Auto-increment ID starts at 1

    def add_user(self, name, email):
        user = User(self.next_id, name, email)
        self.users.append(user)
        self.next_id += 1
        print(Fore.GREEN + "User added successfully.")

    def view_users(self):
        if not self.users:
            print(Fore.YELLOW + "No users found.")
        else:
            print(Fore.CYAN + "\nList of Users:")
            for user in self.users:
                print(Fore.CYAN + str(user))

    def update_user(self, user_id, new_name, new_email):
        for user in self.users:
            if user.user_id == user_id:
                user.name = new_name
                user.email = new_email
                print(Fore.GREEN + "User updated successfully.")
                return
        print(Fore.RED + "User not found.")

    def delete_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                self.users.remove(user)
                print(Fore.GREEN + "User deleted successfully.")
                return
        print(Fore.RED + "User not found.")

# ----- Menu System -----
manager = UserManager()

while True:
    print(Style.BRIGHT + Fore.MAGENTA + "\nUser Management Menu")
    print("1. Add User")
    print("2. View Users")
    print("3. Update User")
    print("4. Delete User")
    print("5. Exit")

    choice = input(Fore.YELLOW + "Choose an option (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        manager.add_user(name, email)

    elif choice == "2":
        manager.view_users()

    elif choice == "3":
        try:
            user_id = int(input("Enter user ID to update: "))
            new_name = input("Enter new name: ")
            new_email = input("Enter new email: ")
            manager.update_user(user_id, new_name, new_email)
        except ValueError:
            print(Fore.RED + "Invalid input. ID must be a number.")

    elif choice == "4":
        try:
            user_id = int(input("Enter user ID to delete: "))
            manager.delete_user(user_id)
        except ValueError:
            print(Fore.RED + "Invalid input. ID must be a number.")

    elif choice == "5":
        print(Fore.GREEN + "Exiting program.")
        break

    else:
        print(Fore.RED + "Invalid choice. Please select 1–5.")
