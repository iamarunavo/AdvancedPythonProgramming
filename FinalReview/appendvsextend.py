lst1 = [1,2,3]
lst1.append([4,5]) # Adds as a single element
print(lst1) # Output: [1, 2, 3, [4, 5]]

lst2 = [1,2,3]
lst2.extend([4, 5]) #Adds each element individually
print(lst2) # Output: [1, 2, 3, 4, 5]
