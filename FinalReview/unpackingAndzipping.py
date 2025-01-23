lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates #unpacking
print(latitude)
print(longitude)

a,b,*rest = range(5) #unpacking using star
print(a,b,rest) 

c=[1,2,3]
d = ['a', 'b', 'c']
zipped1 = list(zip(c,d)) #zipping
print((zipped1))

e = [1,2,3] 
f = ['a', 'b']
zipped2 = list(zip(e,f)) #zipping different length
print(zipped2)

pairs = [(1,'a'), (2,'b'), (3,'c')]
numbers, letters = zip(*pairs) #unzipping using zip
print(numbers)
print(letters)

#using zip to create dict when you havbe two lists
keys = ['a','b', 'c']
values = [1,2,3]
dictionary = dict(zip(keys,values))
print(dictionary)


#practical use of zip
matrix = [[1,2,3], [4,5,6], [7,8,9]]
transpose = [list(row) for row in zip(*matrix)]
print(transpose) 
