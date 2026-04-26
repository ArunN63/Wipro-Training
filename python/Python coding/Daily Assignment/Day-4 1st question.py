class Bankaccount:
    def __init__(self, acc_no,name,balance):
        self.__acc_no=acc_no
        self.__name=name
        self.__balance=balance
    def get_acc_no(self):
        return self.__acc_no
    def get_name(self):
        return self.__name
    def get_balance(self):
        return self.__balance
    def set_name(self,name):
        self.__name=name
    def set_balance(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
        print("Deposited:",amount)
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print("Withdraw:",amount)
        else:
            print("Insufficient balance")
    def display(self):
        print("Account No:",self.__acc_no)
        print("Name:",self.__name)
        print("Balance:",self.__balance)
acc1=Bankaccount(101,"Mohan",5000)
acc1.display()
acc1.deposit(2000)
acc1.withdraw(2000)
acc1.display()

