
class User:
    def __init__(self, user_id, user_name, user_email):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email

    def __str__(self):
        return f"ID: {self.user_id} | Name: {self.user_name} | Email: {self.user_email}"
