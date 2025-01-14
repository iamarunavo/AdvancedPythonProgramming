def track_execution(func):
    count = 0
    def wrapper():
        nonlocal count
        count+=1
        func()
        print("Execution count: ", count)
    return wrapper

@track_execution
def say_hello():
 print("Hello")
say_hello()
say_hello()
# Expected Output:
# Hello
# Execution count: 1
# Hello
# Execution count: 2