

def evenGen():
    count = 2
    def f():
       nonlocal count
    while count<10:
        result = count
        count+=2
        return result
        
    return f

print(f())
print(f())