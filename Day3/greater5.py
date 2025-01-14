num1=int(input("Enter the first integer: "))
num2=int(input("Enter the second integer: "))
num3=int(input("Enter the third integer: "))
num4=int(input("Enter the fourth integer: "))
num5=int(input("Enter the fifth integer: "))

maxNum = num1
if num2>maxNum:
    maxNum = num2
if num3>maxNum:
    maxNum = num3
if num4>maxNum:
    maxNum = num4
if num5>maxNum:
    maxNum = num5

print(maxNum)
