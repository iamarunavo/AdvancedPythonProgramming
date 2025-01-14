n=int(input("Enter a positive integer where the rightmost digit is not zero: "))
if n%10==0 or n==0:
    print("Invalid input")
else:
    while n>=1:
        print(n%10,end="")
        n=n//10