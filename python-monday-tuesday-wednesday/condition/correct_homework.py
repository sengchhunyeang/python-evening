# Homework

# caculator score's student at ICT
# input subject 3 (  Python<=50 and Java=<=50 and NextJs<=50) Note : score 0 to <=50
# chek condition if total score smaller then 49 student fail
# if score's student greater then 50 to 70 student is pass
# if score's student greater then 70 to 100 student is passed and having cado (Example : Book pen bag )
# bunus : for color style and design 10 point
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
END = "\033[0m"
print("============Caculator score's student at ICT=========")
print("Enter score don't greater then 50 ")
print("if enter number greatter then 50 program Exit ") # block test 1
python = float(input("enter python score: ")) # input float float funtion 
if python > 50:
    print(f"{RED}typing number greater then 50{END}")
    exit()  # block test 2 
java = float(input("enter java score: ")) # input float 
if java > 50:
    print(f"{RED}typing number greater then 50{END}")
    exit() # block test 3
nextJs = float(input("enter nextJs score: "))
if nextJs > 50:
    print(f"{RED}typing number greater then 50{END}")
    exit() # # block test 4
totalscore = python + java + nextJs #totalScore = all subject count (total : 73.7) #Test 5
print(f"Total score : {totalscore}") # print total score  

if(totalscore>=50 and totalscore<=70): # true and false = false 
    print("Student pass ") # no working
elif(totalscore>=70):  
    print("Student pass have Kado") #Test 6


