# caculator.py
import math


def average(sub1, sub2, sub3):
    # find average
    result = sub1 + sub2 + sub3 / 3
    return result


def grade(average):
    A = 90
    B = 80
    C = 70
    D = 60
    E = 50
    F = 49
    if average >= A:
        print("your grade A")
    elif(average>=B and average<A):
        print("Your grade B")
    elif average >=C and average <B:
        print("Your grade C ")
    elif average >=D and average <C:
        print("Your Grade D")
    elif average >=E and average <D:
        print("Your Grade E")
    else:
        print("Your grade F Your are Fail")
