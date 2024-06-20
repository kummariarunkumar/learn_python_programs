print('hello')

# <----------------------------------------------------------------->

# 1. Addition
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
result=num1+num2
print(f"sum:{num1}+{num2}={result}")

# <----------------------------------------------------------------->

# 2. Division
num1=float(input("Enter a divident for Division"))
num2=float(input("Enter a divisor for Division"))
if num2==0:
    print("Error: Division by zero is not allowed.")
else:
    result=num1/num2
    print(f"Division :{num1}/{num2}={result}")
    
# <----------------------------------------------------------------->

# 3.Write a Python program to find the area of a triangle.
#area of the triangle formula =half*base*height {take half=0.5}
base=float(input("Enter the value of base"))
height=float(input("Enter the value of height"))
area=0.5 * base * height
print(f"Area of Triangle:{area}")

<----------------------------------------------------------------->

# 4. Write a Python program to swap two variables

a=input("Enter a number")
b=input("Enter a number")
print(f"original values: a value ={a}, b value={b} ")
temp=a
a=b
b=temp
print(f"Swapped values: a values={a}, b value={b}")

# <----------------------------------------------------------------->
# 5. Write a Python program to generate a random number.

import random
print(f"random number:{random.randint(1,1000)}")

#<----------------------------------------------------------------->

# 6. Write a Python program to convert kilometers to miles
km=float(input("Eter distance in kilometer"))
con=0.621371
miles=km*con
print(f"{km} kilometer is equal to {miles} miles ")

#<----------------------------------------------------------------->

#7. Write a Python program to convert Celsius to Fahrenheit.
celsius=float(input("Enter temperature in celcius"))
f_heat=(celsius*9/5)+32
print(f"{celsius} degree celcius is equal to {f_heat} degrees")

#<----------------------------------------------------------------->

#8. write a ython program to display calender

import calendar
year=int(input("Enter year:"))
month=int(input("Month:"))

cal=calendar.month(year,month)
print(cal)

#<----------------------------------------------------------------->

#9. write a python program to solve the quadratic equation
import math
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
eq=b**2-4*a*c
if eq>0:
    root1=(-b+math.sqrt(eq))/(2*a)
    root2=(-b-math.sqrt(eq))/(2*a)
    print(f"Root 1:{root1}")
    print(f"Root 2:{root2}")
elif eq==0:
    root=-b/(2*a)
    print(f"Root:{root}")
else:
    real_part=-b/(2*a)
    img_part=math.sqrt(abs(eq))/(2*a)
    print(f"Root 1: {real_part}+{img_part}i")
    print(f"Root 2: {real_part}-{img_part}i")

#<----------------------------------------------------------------->

#10. write a python program to swap two variables without temp variavble
a=5
b=4
a,b=a,a
print("After swapping")
print("a=",a)
print("b=",b)


#<----------------------------------------------------------------->

#11. Write a Python Program to Check if a Number is Positive, Negative or Zero.
num=float(input("Enter a number"))
if num>0:
    print("Positive numbers")
elif num==0:
    print("Zero")
else:
    print("Negative number")

#<----------------------------------------------------------------->

#12. Write a Python Program to Check if a Number is Odd or Even.
num=int(input("Enter any number"))

if num%2==0:
    print("This is even number")
else:
    print("This is a odd number")

#<----------------------------------------------------------------->
       
#13. write a python program to check leap year
year=int(input("Ënter a year: "))
if (year%400==0) and (year%100==0):
    print("{0} is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 !=0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))

#<----------------------------------------------------------------->

#14. write a program to check prime number
num= int(input("Enter a number"))

flag=False

if num == 1:
    print(f"{num}, is not a prime number")
elif num > 1:
    for i in range(2, num):
        if(num % i) == 0:
            flag=True
            break
if flag:
    print(f"{num}, is not a prime number")
else:
    print(f"{num}, is a prime number")
    
#<----------------------------------------------------------------->

#15. write a python program to print all prime numbers in an interval of 1-10

lower=1
upper=10

print("Prime numbers between", lower,"and",upper,"are")

for num in range(lower,upper+1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)
                
#<----------------------------------------------------------------->

#16. Write a Python Program to Find the Factorial of a Number.
num=int(input("Enter a number"))
factorial=1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num ==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"The factorial of {num} is {factorial}")

#<----------------------------------------------------------------->

#17. write a program to display the multiplication Table
num=int(input("Enter a number"))

for i in range(1,11):
    print(f"{num}x{i}={num*i}")

<----------------------------------------------------------------->

#18. write a ppython program to frint the fibonacci sequence
nterms=int(input("How many terms?"))
n1,n2=0,1
count=0
if nterms<=0:
    print("Enter positive numbers")
elif nterms==1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci Sequence:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n2=nth
        count+=1
        
