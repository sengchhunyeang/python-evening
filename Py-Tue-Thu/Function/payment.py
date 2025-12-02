
def pay_food(withdraw):
    global back_transfer
    rice = 4000
    if withdraw > rice :
       back_transfer= withdraw-rice
    return back_transfer
def pay_check(withdraw):
    global bak_transfer
    checken = 3000
    if withdraw > checken:
        bak_transfer = withdraw-checken
        return bak_transfer
my_money = 10000

payment = pay_food(my_money)
print(payment)
payment2 = pay_check(payment)
print(payment2)

print("Total",payment+payment2)
