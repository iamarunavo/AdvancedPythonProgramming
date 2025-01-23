from random import randint

n = int(input("Enter amount of rows: "))
m = int(input("Enter amount of columns: "))
k = int(input("Enter max value for elements: "))

if k < n * m:
    raise Exception("The max value for elements must be greater than or equal to the size of the matrix.")
    
x = []
seen = []

for i in range(n):
    row = []
    for j in range(m):
        newElement = randint(1, k)
        while newElement in seen:
            newElement = randint(1, k)
        row.append(newElement)
        seen.append(newElement)
x.append(row)

for row in x:
    print(row)

#using set
n = int(input("Enter amount of rows: "))
m = int(input("Enter amount of columns: "))
k = int(input("Enter max value for elements: "))

if k < n * m:
    raise Exception("The max value for elements must be greater than or equal to the size of the matrix.")

x = []
seen = set()

for i in range(n):
    row = []
    for j in range(m):
        newElement = randint(1, k)
        while newElement in seen:
            newElement = randint(1, k)
        row.append(newElement)
        seen.add(newElement)
x.append(row)

for row in x:
    print(row)