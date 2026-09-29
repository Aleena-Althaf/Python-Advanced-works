#create a class shapes with two methods get_area and get_perimeter
#create two subclasses
#rectangle and square

# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#
#     @abstractmethod
#     def get_area(self):
#         pass
#
#     @abstractmethod
#     def get_perimeter(self):
#         pass
#
# class Rectangle(Shape):
#
#     def __init__(self):
#         self.length=int(input("entr the length:"))
#         self.breadth=int(input("enter the breadth:"))
#
#     def get_area(self):
#         print("Area of rectangle:",self.length*self.breadth)
#
#     def get_perimeter(self):
#         print("Perimeter of rectangle:",2*(self.length+self.breadth))
#
#
# class Square(Shape):
#     def __init__(self):
#         self.side=int(input("enter the side:"))
#
#     def get_area(self):
#         print("Area of square:",self.side*self.side)
#
#     def get_perimeter(self):
#         print("Perimeter of square:",4*self.side)
#
#
# r=Rectangle()
# r.get_area()
# r.get_perimeter()
#
# s=Square()
# s.get_area()
# s.get_perimeter()
#******************************************************************************
#create an abstract class Employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee  >>additional property:monthly_salary
# -PartTimeEmployee  >>additional property:rate and hours
# Each class should calculate salary differently
#each employee should have properties:name,age,empid


from abc import ABC,abstractmethod
class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

    def __init__(self):
        self.name=input("enter the employee name:")
        self.age=int(input("enter the age:"))
        self.empid=int(input("enter the empid:"))

class Fulltimeemployee(Employee):

    def __init__(self):
        super().__init__()
        self.monthly_salary=int(input("enter the  monthly salary:"))

    def calculate_salary(self):
        print("total full time salary:",self.monthly_salary)

class Parttimeemployee(Employee):

    def __init__(self):
        super().__init__()
        self.rate=int(input("enter the rate:"))
        self.hours=int(input("enter the hour:"))

    def calculate_salary(self):
        print("total part time salary:", self.rate*self.hours)

e1=Fulltimeemployee()
e1.calculate_salary()

e2=Parttimeemployee()
e2.calculate_salary()
