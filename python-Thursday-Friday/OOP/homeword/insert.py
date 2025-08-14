class Users:
    _userId = 0
    def __init__(self,userName,email):
        self.userId = Users._userId
        Users._userId+=1
        self.userName = userName
        self.email = email
    def show(self):
        print("=================Show Imformation ======================")# this method only show data form class 
        print(f"{self.userName} ID :",self._userId)
        print(f"name {self.userName}")
        print(f"{self.userName}Email :{self.email}")
        print("=================END======================")# this method only show data form class 
        


userName = str(input("Enter name :"))
email = str(input("Email:"))

# create object 
obj = Users(userName,email)

obj.show() # show all information data form class
