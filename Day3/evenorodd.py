#way1
num = int(input("Please enter an integer: "))
if num%2==1:
    print(num, " is odd")
    
print(num, " is even")

#way2
num2= int(input("Please enter an integer: "))
if num%2==0:
    print(num, " is even")
if num%2!=0:
    print(num, " is odd")

#way3
number = int(input("Please enter an integer: "))
if number % 2 == 0:
    print(f"{number} is even.")
if number % 2 == 1:
    print(f"{number} is odd")