from page.Store import *


def homepageMenu():
    print("1-Store\n2-Smart Schedule\n3-budget\n4-Profile\n5-Customer ")


def getOption(opt):

        if opt == '1':
            cafeStoreName()

        elif opt == '2':
            print("2-Smart schedule ")
        elif opt == '3':
            print("3-Budget")
        elif opt == '4':
            print("4-Profile")
        elif opt == '5':
            print("5-Customer ")

def cafeStoreName():
    print("1-H1Shop\n2-H1Shop \n3-H3Shop ")

def optionStore(opt):
    if opt == '1':
        print(cafe["price"],"$")
    elif opt == '2':
        print(dessert)
    elif opt == '3':
        print("3-H3Shop")
