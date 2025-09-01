#Task 1
#check number if even or odd

num=int(input('Enter the number:'))

if(num%2==0):
    print("Number is Even")
else:
    print("Number is Odd")

print("Thankyou")



#Task2
#Sum of integers from 1 to 50

sum=0
for i in range(1,51):
    sum=sum+i

print('The sum of numbers from 1 to 50 is:',sum)