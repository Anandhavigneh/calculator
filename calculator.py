# PROGRAM TO MAKE A MINI CALCULATOR USING FUNCTIONS

# create functions

def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x%y

#GETTING CHOICES FROM THE USER

print("1.addition \n2.subtraction \n3.multiplication \n4.division")
choices=int(input("enter the number 1,2,3,4: \n"))

#GETTING INPUT FROM THE USER

num1= int(input("ENTER THE FIRST NUMBER: \n"))
num2= int(input("ENTER THE SECOND NUMBER: \n"))

#CONDITION

if choices==1:
    print("your value is: ",add(num1,num2))
elif choices==2:
    print("your value is: ",subtract(num1,num2))
elif choices==3:
    print("your value is: ",multiply(num1,num2))
elif choices==4:
    print("your value is: ",divide(num1,num2))
else:
    print("invalid choice")

print("thank you")

    