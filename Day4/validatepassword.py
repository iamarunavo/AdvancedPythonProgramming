attempts = 0
while attempts <= 3:
    password=int(input("Enter a password that is a two digit integer, where both digits are even: "))
    if password > 99 or password < 10:
        attempts+=1
        print("Invalid password. Try again")
    else:
        firstDigit = password//10
        secondDigit = password%10
        if firstDigit%2==0 and secondDigit%2==0:
            attempts+=1
            print("Correct! You may access the system.")
            break
        else:
            attempts+=1
            print("Invalid password. Try again")
    if attempts>3:
        print("Too many invalid attempts. Try again later")

