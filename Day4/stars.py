n=int(input("Enter a positive integr: "))
if n < 1:
    print("Invalid input")
else:
    i = 1
    while i <= n:
        print("*" * i)
        i+=1
