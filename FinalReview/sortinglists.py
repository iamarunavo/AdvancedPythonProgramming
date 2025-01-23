#sorting with lambda
data = [(1, 'b'), (3, 'a'), (2, 'c')]
sorted_data1= sorted(data, key=lambda x: x[1])  # Sort by the second element
print(sorted_data1) # Output: [(3, 'a'), (1, 'b'), (2, 'c')]

def get_second_element(item):
    return item[1]

sorted_data2= sorted(data, key=get_second_element)
print(sorted_data2) # Output