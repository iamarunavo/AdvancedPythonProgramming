sumeven=0
mylist=[]
for i in range(1, 11):
    mylist.append(i)
    if i%2==0:
        sumeven+=i

print(mylist)
print(sumeven)