class CreditCard:
    def __init__(self, customer, bank, balance, CardNo):
        self.customer = customer
        self.bank = bank
        self.CardNo = CardNo
        self.balance = balance

    def get_customer(self):
        return self.customer
    def get_bank(self):
        return self.bank
    def get_CardNo(self):
        return self.CardNo
    def get_balance(self):
        return self.balance
    def make_payment(self,amount):
        self.balance -=amount
cc = CreditCard("venky","SBI",100000,"7830692507148256")
cc.make_payment(int(input("make payment of  :")))
print("remaining balance:",cc.get_balance())


# output:
# make payment of  :20000
# remaining balance: 80000