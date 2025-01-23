from collections import Counter

invertedDict = {}

with open('Day12/address.txt', 'r') as file: #opening and reading a file
    for line_number, line in enumerate(file, start=1):
        # Split the line into words
        words = line.strip().split()
        
        for word in words:
            # Convert the word to lowercase (optional) for case insensitivity
            word = word.lower()
            
            # Initialize the dictionary entry if it doesn't exist
            if word not in invertedDict:
                invertedDict[word] = []
            
            # Append the line number as many times as the word appears on the line
            occurrences = words.count(word)
            invertedDict[word].extend([line_number] * occurrences)



print(invertedDict['men'])


def squish(x):
    counter = Counter(x)
    result = list(counter.items())
    return result


print(squish([4,4,4,6,6,8,8,8,8]))