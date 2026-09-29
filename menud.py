#menu driven progrm for a calculator
# def add():
#     n1=int(input("enter num1:"))
#     n2 = int(input("enter num2:"))
#     s=n1+n2
#     print("sum:",s)
# def sub():
#     n1=int(input("enter the number1:"))
#     n2=int(input("enter the number2:"))
#     s=n1-n2
#     print("difference:",s)
#
#
# while(True):
#     print("1.add")
#     print("2.sub")
#     print("3.mul")
#     print("4.div")
#     print("5.exit")
#     ch=int(input("enter the choice:"))
#     if ch==1:
#         add()
#     elif ch==2:
#         sub()
#     elif ch==3:
#         print("mul")
#     elif ch==4:
#         print("div")
#     else:
#         print("exiting")
#         break
#******************************************************
#menu driven program to fil read write append search and exit
def fileread():
    fn=input("enter the file name:")
    f=open(fn,"r")
    content=f.read()
    f.close()
def filewrite():
    fn=input("enter the file name:")
    f=open(fn,"w")
    w=input("enter the contents:")
    content=f.write(w)
    f.close()
def fileappend():
    fn=input("enter the file name:")
    f=open(fn,"a")
    f.write("hai hello ")
    f.close()
def filesearch():
    fn=input("enter the file name:")
    f=open(fn,"r")
    content=f.read()
    a=input("enter the word to search:")
    if a in content:
        print("the word is present")
    else:
        print("the word is not present")
    f.close()
def filedelete():
    import os
    fn=input("enter the file name:")
    os.remove("k.txt")
    print("file deleted")

while (True):
    print("Menu driven operations")
    print("1.Fileread")
    print("2.Filewrite")
    print("3.Fileappend")
    print("4.Filesearch")
    print("5.Filedelete")
    print("6.exit")
    ch=int(input("enter the choice:"))
    if ch==1:
        fileread()
    elif ch==2:
        filewrite()
    elif ch==3:
        fileappend()
    elif ch==4:
        filesearch()
    elif ch==5:
        filedelete()
    else:
        print("exiting...")
        break

