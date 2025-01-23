def my_bin(n):
    reversebinary=""
    while n>0:
        reversebinary+=str(n%2)
        n//=2
        
    binary = reversebinary[::-1]
    return binary


print(my_bin(12))

