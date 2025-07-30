RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
END = "\033[0m"
# 18 to 30 morality 
# pass_BacII
personal = int(input("Enter your age :"))
bacII = input("your are pass bacII yes/no:")
if(bacII=="yes"): # True 
    if(personal>=18 and personal<=30):
     print(f"{personal}{GREEN}can be soilder{END} ")
    else:
        print("can not pls stay at your working for learn money")
else :
    print(f"{RED}pls study on hight school !{END}")
    
# Nested Condition 

# Homework 

# caculator score's student at ICT
# input subject 3 (  Python<=50 and Java=<=50 and NextJs<=50) Note : score 0 to <=50 
# chek condition if total score smaller then 49 student fail 
# if score's student greater then 50 to 70 student is pass 
# if score's student greater then 70 to 10 student is passed and having cado (Example : Book pen bag )
# bunus : for color style and design 10 point 