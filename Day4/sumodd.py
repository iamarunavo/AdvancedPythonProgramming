n=int(input("Enter a positive integer: "))
if n < 1:
    print("Invalid input")
else:
    sumF = 0
    i = 1
    while i <= n:
        if i%2!=0:
            sumF+= i
        i+=1

print(sumF)