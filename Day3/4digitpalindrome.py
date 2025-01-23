fourdigit=int(input("Enter a four digit number: "))
if fourdigit <= 999 or fourdigit > 9999:
    print("Not within the given range")
else:
    firstdigit = fourdigit//1000
    seconddigit = (fourdigit//100) % 10
    thirddigit = (fourdigit//10) % 10
    fourthdigit = fourdigit % 10

    if firstdigit==fourthdigit and seconddigit==thirddigit:
        print(fourdigit, "is a palindrome number")
    else:
        print(fourdigit, "is not a palindrome number")