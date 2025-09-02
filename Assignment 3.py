#Task 1:
#calculate factorial using function

def fact(x):
    if (x<1):
        print("incorrect input")
    else:
        f=1
        for i in range(1,x+1):
            f=f*i
        return f

a=int(input('Enter the number to find factorial:'))
result=fact(a)
print(result)




#Task 2:

x=int(input('Enter a number:'))
from math import *
s=sqrt(x)
l=log(x,e)
t=sin(x)

print("Square of the number is ",s)
print("log of the number is ",l)
print("Sine of the number is ",t)


