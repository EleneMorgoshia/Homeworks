#homework:
#use  input, %,if ,+= ; and 
#ask user to enter 3 numbers.then sum the odd numbers and print . 
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
num3=int(input("enter num3: "))

variable1=num1%2
if variable1==1:
    print("num1 is an odd number")
    variable1=num1
else:
    print("num1 is not an  odd number")
    variable1=0

variable2=num2%2
if variable2==1:
       print("num1 is an  odd number")
       variable2=num2
else:
    print("num1 is not an odd number")
    variable2=0

variable3=num3%2
if variable3==1:
     print("num1 is an odd number")
     variable3=num3
else:
    print("num1 is not an  odd number")
    variable3=0

print(variable1+variable2+variable3)