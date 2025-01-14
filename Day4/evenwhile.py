n = int(input("Enter a pos integer: "))
a=1
while n >= 2:
    while a <= n:
        if a % 2 == 0:
            print(a)
        a += 1  # Increment a outside the if statement


userInput = int(input("Enter a positive integer greater than or equal to 2: "))
if userInput < 2:
    print("Invalid input.")
else:
    i = 1
    while i <= userInput:
        print(i) if i % 2 == 0 else None
        i += 1