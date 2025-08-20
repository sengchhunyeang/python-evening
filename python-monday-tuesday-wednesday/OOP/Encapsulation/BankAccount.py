class BankAccount:
    def __init__(self, acc_id, acc_name, acc_balance):
        self.acc_id = acc_id
        self.acc_name = acc_name
        self.__acc_balance = acc_balance
    # setter
    def set_balance(self, balance):

        self.__acc_balance = balance

    # getter
    def get_balance(self):

        return self.__acc_balance


acc = BankAccount(acc_id=12, acc_name="ABC", acc_balance=100)
balance = float(input("input balance :"))
print(f"balance:{balance}$")
acc.set_balance(balance)
print(acc.acc_id)
print(acc.acc_name)
print(acc.get_balance())
get_bal = acc.get_balance()
mybalance = 100
totalbalance = get_bal + mybalance
print("my total balance ",totalbalance ,"$")

