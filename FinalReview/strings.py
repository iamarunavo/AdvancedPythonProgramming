#strings are immutable, they can't be modified
#strings are iterables so we use "for"
#strings are sequences, so we can access elements and substrings them []
#we can concatenate strings

#string functions
#str.count(sub[,start[,end]]) #counts occurences of substring within given range
#str.find(sub[,start[,end]]) #finds lowest index of substring within given range
#str.join(iterable)
#str.replace(old,new[,count]) #return copy of string with occurences of substring replaced by new
#str.split([sep[,maxsplit]]) #return a list of words in the string using sep as delimeter, if maxsplits is given then string is by maxsplits times
#str.rstrip([chars]) #returns copy of string with chars removed
#str.lstrip([chars])
#str.strip([chars])
#str.upper()
#str.lower()

text1 = "banana banana banana"
print(text1.count("banana"))  # Output: 3
print(text1.count("banana", 7))  # Output: 2 (starts from index 7)
print(text1.count("banana", 7, 13))  # Output: 1 (range is 7 to 13)

text2 = "hello world, welcome to the world"
print(text2.find("world")) #Output: 6
print(text2.find("world", 7)) #Output 28
print(text2.find("world",7, 23)) #Output: -1, since it wasn't found

words = ["Python", "is", "awesome"]
delimiter = " "
print(delimiter.join(words))  # Output: "Python is awesome"

# Example with a tuple
letters = ('A', 'B', 'C')
print("-".join(letters))  # Output: "A-B-C"

text3 = "apple apple orange apple"
print(text3.replace("apple", "banana"))  # Output: "banana banana orange banana"
print(text3.replace("apple", "banana", 2))  # Output: "banana banana orange apple"

text4="Today was a great day"
print(text4.split(" "))
print(text4.split(" ", 2))
