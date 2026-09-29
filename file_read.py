# f=open("w.txt",'r')
# s=f.read()
# # a=f.readlines()
# print(s)
# # print(type(s))
# # print(a)
# # print(type(a))
# f.close()

# # #write a program to read a text file and displays the number of lines in a file
# f=open("w.txt",'r')
# s=f.readlines()
# print(len(s))
# f.close()
#**********************************************
# # #write a program to display the number of words in a file
# f=open("w.txt",'r')
# s=f.read()
# a=s.split()
# b=len(a)
# print(b)
# f.close()

# # #write a program to update the second line in a file
# f=open('w.txt','r')
# s=f.readlines()
# s[1]='computer\n'
# f.close()
# f=open('w.txt','w')
# f.writelines(s)
# f.close()
#*****************************************************
# # #write a program to display the last 5 lines in a file
# f=open('w.txt','r')
# s=f.readlines()
# print(s[-5:])
# f.close()
#*****************************************************
# #program to search a particular word in a file
# f=open('w.txt','r')
# s=f.read()
# a=input("enter a string:")
# if   a in s:
#     print("present")
# else:
#     print("not present")
# f.close()
#**************************************88
# #find the number of letters,digits,and spaces in a file
# f=open("w.txt","r")
# s=f.read()
# l=0
# d=0
# sp=0
# for i in s:
#     if i.isalpha():
#         l+=1
#     elif i.isdigit():
#         d+=1
#     else:
#         sp+=1
# print("l count:",l)
# print("d count:",d)
# print("sp count:",sp)
# f.close()
#************************************************

#reverse the lines in a file
# f=open("w.txt","r")
# s=f.readlines()
# a=s[::-1]
# print(a)
# f.close()

# A file totalstudents.txt contains the names of all students in a class,
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
# Write a Python program to:
# Read the names from both files.
# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per lin
#******************************************************8
#append mode
# f=open("w.txt","a")
# f.write("python")
# f.close()
#***********************************88
#write a program to read the content from one text file and add that content into another file
# f=open("w.txt","r  ")
# s=f.read()
# f.close()
# f=open("a.txt","a")
# f.write(s)
# f.close()
#******************************
# f=open("w.txt","a+")
# f.write("pythonn")
# print(f.read())
# f.close()
#*******************************
#seek and tell funcion example
# f=open("a.txt","a+")
#
# print(f.tell())
# f.write("python")
# print(f.tell( ))
# print(f.seek(0))
# print(f.read())
# #print(f.seek())
# f.close()
#*********************************8888
# import os
# os.remove("a.txt")
# print("File is deleted ")
#**************************************




