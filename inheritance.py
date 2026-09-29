#inheritance
#
# class Parent:
#     def m1(self):
#         print("parent class method m1")
#     def m2(self):
#         print("parent class method m2")
# class Child(Parent):
#     def m1(self):
#         super().m1() #to run m1 of parent
#
#         print("child class method m1")
#     def m3(self):
#         print("child class method m3")
# c=Child()
# c.m1()
# c.m2()
# c.m3()


# class Person:
#     def __init__(self):
#         self.name=input("enter the name:")
#         self.age=int(input("enter the age:"))
#     def show(self):
#         print(self.name,self.age)
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.rollno=int(input("enter the rollno:"))
#         self.course=input("enter the course:")
#         self.mark=int(input("enter the marks:"))
#     def show(self):
#         super().show()
#         print(self.rollno, self.course,self.mark)
#     def update(self):
#         self.mark=int(input("enter the new mark:"))
#
# s=Student()
# s.show()
# s.update()


class Company:
    def __init__(self):
        self.company_name=input("enter the company name:")
        self.location=input("enter the location")

    def display_company(self):
        print(self.company_name,self.location)

class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid=int(input("enter the empid:"))
        self.name=input("enter the anme:")
        self.designation=input("enter the designation:")
        self.salary=int(input("enter the salary:"))
    def display_details(self):
        super().display_company()
        print(self.empid,self.name,self.salary,self.designation)
    def updatesalary(self):
        self.salary=1.1*self.salary
        print("updated salary:",self.salary)
e=Employee()
e.display_details()
e.updatesalary()





