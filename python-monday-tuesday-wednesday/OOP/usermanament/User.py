class User:
    #constructor User
    def __init__(self, user_id, user_name, user_email):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email

        # return string
    def __str__(self):
        return f"userId:{self.user_id}, userName:{self.user_name}, userEmail:{self.user_email}"
