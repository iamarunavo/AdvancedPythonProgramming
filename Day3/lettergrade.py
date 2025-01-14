score = int(input("Please enter your score: "))
if score>100 or score<0:
    print("Score out of range")
elif score>=90:
    print("A")
elif (80<=score<90):
    print("B")
elif (70<=score<80):
    print("C")
elif (60<=score<70):
    print("D")
elif score<60:
    print("F")
