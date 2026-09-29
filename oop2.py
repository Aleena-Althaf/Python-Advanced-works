#write a menu driven code fr bank peration using class and list
#create a new acount
#withdraw
#deposit
#showbalance
#exit

class Account:
    def __init__(self):
        print("account details")
        self.accntnumber=int(input("enter the account number:"))
        self.accntname=input("enter the account name:")
        self.balance=int(input("enter the balance:"))
    def showbalance(self):
        print("current balance:",self.balance)
    def withdraw(self):
        amount=int(input("enter the amount to withdraw:"))
        if amount>self.balance:
            print("n sufficint balance")
        else:
            self.balance=self.balance-amount
            print("blance after withdrawal is:",self.balance)

    def deposit(self):
        amount=int(input("enter the amount to deposit:"))
        self.balance=self.balance+amount
        print("balance after deposit is:",self.balance)
l=[]
while(True):
    print("Bank operations")
    print("1.create a new account")
    print("2.withdraw")
    print("3.deposit")
    print("4.show balance")
    print("5.exit")
    ch=int(input("enter the choice:"))
    if ch==1:
        a=Account()
        l.append(a) #saves each account objects into a list
        print(a)
    elif ch==2:
        a=Account()
        num=int(input("enter the aacnt num:"))
        for i in l:
            if(i.accntnumber==num):
                i.withdraw() 


