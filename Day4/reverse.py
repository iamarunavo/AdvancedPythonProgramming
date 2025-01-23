num=int(input("Enter a three digit integer: "))

if num < 100 or num > 999:
    print("Invalid input")
if num % 10 == 0:
    print("Invalid input! The number cannot have a zero in the units position.")

hundreds = num // 100         
tens = (num // 10) % 10        
units = num % 10

print(units,tens,hundreds)
