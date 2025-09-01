# Python
# Assignment 1
# Task 1
a=int(input('Enter the first number:'))
b=int(input('Enter the second number:'))
add=a+b
s=a-b
m=a*b
d=a/b

print('Addition:',add)
print('Subtraction:',s)
print('Multiplication:',m)
print('Division:',d)

# Task 2
fn=str(input('Enter your first name:'))
ln=str(input('Enter your last name:'))
print("Hello,",fn,ln,"! Welcome to the Python program")


# Assignment 2

# Task 1
#check number if even or odd

num=int(input('Enter the number:'))

if(num%2==0):
    print("Number is Even")
else:
    print("Number is Odd")

print("Thankyou")

# Task2
#Sum of integers from 1 to 50

sum=0
for i in range(1,51):
    sum=sum+i

print('The sum of numbers from 1 to 50 is:',sum)
