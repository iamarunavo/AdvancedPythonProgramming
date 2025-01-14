n=int(input("Enter a integer between 1 and 10: "))
if n<1 or n>10:
    print("Invalid input")
else:
    i = n
    while i>=1:
        print("*" * i)
        i-=1
