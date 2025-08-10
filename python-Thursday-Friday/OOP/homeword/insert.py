class Userss:
    def __init__(self,userId,userName,email):
        self.userId = userId
        self.userName = userName
        self.email = email
    def show(self):
        print("=================Show Imformation ======================")# this method only show data form class 
        print(f"{self.userName} ID :",self.userId)
        print(f"name {self.userName}")
        print(f"{self.userName}Email :{self.email}")
        print("=================END======================")# this method only show data form class 
        

userId = str(input("Enter Id :"))
userName = str(input("Enter name :"))
email = str(input("Email:"))

# create object 
obj = Userss(userId,userName,email)

obj.show() # show all imformation data form class 
