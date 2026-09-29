#.Create a class named Circle with an attribute radius.
# Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
# Create an object of the Circle class and call both methods to display the results.
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
class Circle:
    def __init__(self):
        self.radius=int(input("enter the radius:"))
    def getarea(self):
        area=3.14*self.radius*self.radius
        print("area of circle is:",area)
    def getperimeter(self):
        perimeter=2*3.14*self.radius
        print("perimeter is:",perimeter)
c1=Circle()
c1.getarea()
c1.getperimeter()
#************************************************************************************
# 2.Create a class named Account with attributes acctnumber, acctname, and balance.
# Initialize these values using a constructor by taking input from the user. Define the following methods:
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
# Create an object of the class and call the methods to perform withdrawal and deposit operations and display the updated balance.
class Account:
    def __init__(self):
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

a1=Account()
# a1.withdraw()
# a1.deposit()
# a1.showbalance()
a2=Account()

l=[a1,a2]
for i in l:
    if i.accntnumber==101:
        i.showbalance()
    # print(i.accntname,i.accntnumber,i.balance)


#****************************************************************************



