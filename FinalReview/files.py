# output = open('C:\spam', 'w')       # Create output file ('w' means write)
# input = open('data', 'r')          # Create input file ('r' means read)
# input = open('data')               # Same as prior line ('r' is the default)
# aString = input.read()             # Read entire file into a single string
# aString = input.read(N)            # Read up to next N characters (or bytes) into a string
# aString = input.readline()         # Read next line (including \newline) into a string
# aList = input.readlines()          # Read entire file into list of line strings (with \n)
# output.write(aString)              # Write a string of characters (or bytes) into file
# output.writelines(aList)           # Write all line strings in a list into file
# print(value, ..., file='filename') # Write to file "filename" instead of to the screen
# output.close()                     # Manual close (done for you when file is collected)
# output.flush()                     # Flush output buffer to disk without closing any File
# seek(N)                            # Change file position to offset N for next operation
# for line in open('data'):          # Use line file iterators to read line by line
# open('f.txt', encoding='latin-1')  # Python 3.0 Unicode text files (str strings)
# open('f.bin', 'rb')                # Python 3.0 binary bytes files (bytes strings)


with open('FinalReview/test.txt') as file: #reading a file line by line, way1
    for line in file:
        print(line, end="")
    file.close()

file = open('FinalReview/test.txt') #way2
for line in file:
    print(line, end="")
file.close()