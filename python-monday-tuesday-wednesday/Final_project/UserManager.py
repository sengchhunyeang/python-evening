from User import User
from colorama import init, Fore

init()


class UserManager:
    def __init__(self):
        self.users = []
    # Method for add user to list
    def add_user(self, user_id, user_name, user_email):
        self.users.append(User(user_id, user_name, user_email))
        print(f"{Fore.BLUE}Insert successfully{Fore.RESET}")

    # Method for view user from list
    def view_users(self):
        for user in self.users:
            print(
                f"UserID:{Fore.YELLOW}{user.user_id}{Fore.RESET}"
                f"\nUSerName:{Fore.YELLOW}{user.user_name}{Fore.RESET}"
                f"\nUSerEmail:{Fore.YELLOW}{user.user_email}{Fore.RESET}")


