a = [1, 2, 3]
b = a
del a[1]
print(b)

#changing a reflects the same change in b since in this case b is referencing a
#hence they both share the same change