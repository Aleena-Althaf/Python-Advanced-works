# example exception handling
#
# try:
#     n1=int(input("enter the num1:"))
#     n2=int(input("enter the num2:"))
#     s=n1+n2
# except:
#     print("invalid number")
# else:
#     print("sum:",s)
# finally:
#     print("done")
#**********************************************
#example (multiple exception handling
# try:
#     n1=int(input("enter the num1:"))
#     n2=int(input("enter the num2:"))
#     div=n1/n2
#     print("result:",R)
#
# except ZeroDivisionError:
#     print("Zero Division Error")
#
# except ValueError:
#     print("Value Error")
#
# except:
#     print("Error")
##*********************************************************************
# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
# import math
# try:
#     n=int(input("enter the numbr:"))
#     m=math.factorial(n)
# except ValueError:
#     print("Value Error")
# else:
#     print("Factorial:",m)
#*********************************************************************
# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
#
# while (True):
#     print("simple calculator")
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3.multiplication")
#     print("4.Division")
#     print("5.Exit")
#
#     try:
#         ch=int(input("enter the choice:"))
#         if ch==1:
#             n1=int(input("enter the number1:"))
#             n2=int(input("enter the number2:"))
#             sum=n1+n2
#             print("sum:",sum)
#
#         elif ch==2:
#             n1=int(input("enter the number1:"))
#             n2=int(input("enter the number2:"))
#             diff=n1-n2
#             print("difference:",diff)
#
#         elif ch==3:
#             n1=int(input("enter the number1:"))
#             n2=int(input("enter the number2:"))
#             mul=n1*n2
#             print("multiplication:",mul)
#
#         elif ch==4:
#              n1=int(input("enter the number1:"))
#              n2=int(input("enter the number2:"))
#              div=n1/n2
#              print("division:",div)
#
#         elif ch==5:
#              print("exit")
#              break
#
#         else:
#             print("invalid choice")
#     except ValueError:
#        print("ValueError")
#     except ZeroDivisionError:
#         print("Zero division error")
#     except:
#         print("error")
#***************************************************************
# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
# try:
#     fn=input("enter the file name:")
#     f=open(fn,"r")
#     print("filee opened successfully")
# except FileNotFoundError:
#     print("File not found")
#****************************************************************************
#Given a Dictionary
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist
# try:
#     d={"name":"arun","age":23,"place":"ekm"}
#     n=input("enter the key value:")
#     if n in d:
#         print("value found")
#
# except KeyError:
#     print("Key Error")
#*********************************************************************
#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"
# try:
#     n=int(input("enter the number:"))
#     if (n<=0):
#         raise ValueError("number must be positive")
#     else:
#         print(n)
# except ValueError as e:
#     print(e)
#******************************************************
#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")
# class InvalidPasswordError(Exception):
#     pass
# try:
#     p=input("enter the password:")
#     if len(p)<8:
#         raise InvalidPasswordError("password should be 8 characters")
#     else:
#         print("login successfull")
# except InvalidPasswordError as e:
#     print(e)
#**********************************************************************
#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")
# class InsuffientBalanceError(Exception):
#     pass
# balance=5000
# try:
#     amnt=int(input("enter the amount:"))
#     if (amnt>balance):
#         raise InsuffientBalanceError("Not Enough Balance.Transaction Failed")
#     else:
#         print("amount withdrawed")
# except InsuffientBalanceError as e:
#     print(e)
#******************************************************

