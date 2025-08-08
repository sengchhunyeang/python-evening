# END = "\033[0m"
# CYAN = "\033[0;36m"
# LIGHT_GREEN = "\033[1;32m"
# YELLOW = "\033[1;33m"



while True:
    start = int(input("Enter number :"))
    index = 1
    while index <=10:
            print(f"{start} * {index} = {start*index}")
            # print(f"{LIGHT_GREEN}{start}{END} * {YELLOW}{index}{END} = {start*index}")
            index+=1