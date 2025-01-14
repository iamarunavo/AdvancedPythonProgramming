#way1
n=int(input("Enter a pos integer: " ))
while (n>=1):
    print(n)
    n-=1

#way2
userInput = int(input("Enter a positive integer: "))
if userInput < 1:
    print("Invalid input.")
else:
    while userInput > 0:
        print(userInput)
        userInput -= 1
