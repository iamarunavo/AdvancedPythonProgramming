# s = dict() or s = {}  
# Create a new dictionary.

# len(d)
# Return the number of items in the dictionary d.

# d[key]
# Return the item of d with key key. Raises a KeyError if the key is not in the dictionary.

# d[key] = value
# Set d[key] to value.

# del d[key]
# Remove d[key] from the dictionary. Raises a KeyError if the key is not in the dictionary.

# key in d
# Return True if d has a key key, else False.

# key not in d
# Equivalent to not key in d.

# clear()
# Remove all items from the dictionary.

# copy()
# Return a shallow copy of the dictionary.

# dict.fromkeys(seq, value)
# Create a new dictionary with keys from seq and values set to value.

# items()
# Return a new view of the dictionary’s items ((key, value) pairs).

# keys()
# Return a new view of the dictionary’s keys.

#pop(key[,default])


results = {n: n**2 for n in range(10)} #dictionary comprehension
print(results)