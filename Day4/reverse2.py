#way 1
num=int(input("Enter a three digit integer: "))

if num < 100 or num > 999:
    print("Invalid input")
if num % 10 == 0:
    print("Invalid input! The number cannot have a zero in the units position.")

hundreds = num // 100         
tens = (num // 10) % 10        
units = num % 10

reverse = units*100 + tens*10 + hundreds*1
print(reverse)

#way2
userInput = int(input("Please enter a three digit number: "))
if userInput <= 99 or userInput > 999:
    print("Invalid input.")
else:
    firstDigit = userInput // 100
    secondDigit = (userInput // 10) % 10
    thirdDigit = userInput % 10
    reversedNumber = int(str(thirdDigit) + str(secondDigit) + str(firstDigit))

    print(f"Original number: {userInput}")
    print(f"Reversed number: {reversedNumber}")