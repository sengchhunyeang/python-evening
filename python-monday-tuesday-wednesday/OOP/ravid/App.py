# from Login import *
# if __name__ == '__main__':
#         main()
from ravid.module import homepageMenu, getOption, optionStore, cafeStoreName

homepageMenu()
while True:
    var = input("choose option :")
    getOption(var)
    var2= input("Choose Store :")
    optionStore(var2)