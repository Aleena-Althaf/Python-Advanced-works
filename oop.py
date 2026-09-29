#dynamic inputting
# class Person:
#     def __init__(self):   #__init__ used to create a initialize object attributes/properties
#         self.name=input("enter the name:")
#         self.age=int(input("enter the age:"))
#     def show(self):      #self represents current object
#         print(self.name,self.age)
# p1=Person()   #creates object of class person
#                              #it will call __init__() automatically
# p1.show()
# p2=Person()     #creates object of class person
#                              #it will call __init__() automatically
# p2.show()
#*****************************************************
#static inputting
# class Person:
#     def __init__(self,n,a):   #__init__ used to create a initialize object attributes/properties
#         self.name=n
#         self.age=a
#     def show(self):      #self represents current object
#         print(self.name,self.age)
# p1=Person("arun",23)   #creates object of class person
#                              #it will call __init__() automatically
# p1.show()
# p2=Person("anna",25)     #creates object of class person
#                              #it will call __init__() automatically
# p2.show()
#*******************************************************************
#define a class named employee with attributes empid,name,age,place,salary,designation
#and methods getsalary() and showpersondetails()
#create an employee object and call the methods
# class Employee:
#     def __init__(self):
#         self.empid=input("enter the id:")
#         self.name=input("enter the name:")
#         self.age=int(input("enter the age:"))
#         self.place=input("enter the place:")
#         self.salary=int(input("enter the salary:"))
#         self.desig=input("enter the designation:")
#     def getsalary(self):
#         print(self.salary)
#     def getpersondetails(self):
#         print("ID",self.empid)
#         print("name:",self.name)
#         print("age:",self.age)
#         print("place:",self.place)
#         print("designation:",self.desig)
# e1=Employee()
# e1.getsalary()
# e1.getpersondetails()
#********************************************************
#define a class named student with attributes rollno,name,mark1,mark2,mark3
#and methods display() roll no and total mark of a student
#create 2 students objects and call the methods
# class Student:
#     def __init__(self):
#         self.name=input("enter the student name:")
#         self.rollno=int(input("enter the rollno:"))
#         self.mark1=int(input("enter the mark1:"))
#         self.mark2=int(input("enter he mark2:"))
#         self.mark3=int(input("enter the mark3:"))
#     def display(self):
#         print("rollno:",self.rollno)
#         print("total marks:",(self.mark1+self.mark2+self.mark3))
# s1=Student()
# s1.display()
#s2=Student()
# s2.display()
#******************************************************************
#define a class named book with attributes title,author,price,langage
#and methods gettitle() getauthor(),getprice()
#create book object and call the methods

# class Book:
#     def __init__(self):
#         self.title=input("enter the title:")
#         self.author=input("enter the authr:")
#         self.price=int(input("enter the price:"))
#         self.language=input("enter the languafe:")
#     def gettitle(self):
#         print(self.title)
#     def getauthor(self):
#         print(self.author)
#     def getprie(self):
#         print(self.price)
#     def getlanguage(self):
#         print(self.language)
#     def settitle(self):
#         self.title=input("enter the new title:")
#         self.gettitle()
#     def setauthor(self):
#         self.author=input("enter the new author:")
# b=Book()
# b.gettitle()
# b.settitle()
#****************************************************************
#.Create a class named Circle with an attribute radius.
# Use a constructor to initialize the radius by accepting input from the user. Define the following methods:
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
# class Circle:
#     def __init__(self):
#         self.radius=int(input("enter the radius:"))
#     def getarea(self):
#         area=3.14*self.radius*self.radius
#         print("area of circle is:",area)
#     def getperimeter(self):
#         perimeter=2*3.14*self.radius
#         print("perimeter is:",perimeter)
# c1=Circle()
# c1.getarea()
# c1.getperimeter()
#************************************************************************************
