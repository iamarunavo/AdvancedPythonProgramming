#1. Given the following code, what will be the output?
def func(*args, **kwargs): 
    print(args)     
    print(kwargs) 
    
func(1, 2, 3, a=4, b=5)
#Expected output:
#(1, 2, 3)
#{'a': 4, 'b': 5}

#2. Analyze the following code and explain the output:
def func(a, *args, b):
    print(a, args, b)
func(1, 2, 3, 4)
#There wouldnt be any output just an error as b is supposed required to be a keyword in this case, which is not the case in the function defined

#3. Determine whether the following function definition is valid. If not, explain why:
def func(a, b, /, c, *, d):
    return a + b + c + d
#Valid since / and * are used to distinguish between positional and keyword arguments in python
#In this case / is being used to show that a,b are positional and * is being used to show d is keyword
# c can be either

#4. Is there an error in this code? Why or why not?
def func(a, /, b, *, c):
    return a + b + c
func(1, 2, 3)
# Results in error since the call is passing all of the parameters as positional while the function defines a as positional b as keyword and c as either

#5. Analyze the following code and explain the behavior:
def func(a, b, /):
    return a + b
print(func(1, 2))
print(func(a=1, b=2))
#the first print call works since parameters are being passed in as intended
#the second print call results in an error since the parameters are being passed in as keyword when the function defines them as positional

#6. Determine if the following function works as expected. Explain:
def func(*, a, b):
    return a * b
print(func(a=3, b=4))
print(func(3, 4))
#the following code does not work as expected since function puts keyword before positional

#7. Given the following function, what will be the output of each call? Explain:
def func(a, b, /, c, *, d):
    return a, b, c, d
print(func(1, 2, 3, d=4))
print(func(1, b=2, c=3, d=4))
#first call results in an error since c is keyword and in the call its being passed in as positional
#second call results in an error since b is positional and is being passed in as keyword

#8 What is the output of the following code? Explain:
def func(x, y=10):
    return x * y
print(func(5))
print(func(5, 20))
#Expected output:
# 50
# 100 
# Both calls work because y is a positional-or-keyword argument (default values do not restrict how arguments are passed).

#9 Does the following function definition contain any errors? If so, describe them:
'''
def func(a=1, b):
    return a + b
'''
#the error is that the keyword parameter is before the positional

#7. Explain the behavior of the following code. Is there any potential pitfall associated with having a keyword argument being assigned a mutable value?
def func(a, mylist=[]):
    mylist.append(a)
    return mylist
print(func(1))
print(func(2))
#The code does not work as expected because the default mutable argument mylist retains its state across function calls.
#Output:
# [1]
# [1, 2]

