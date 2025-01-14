def make_counter(start: int = 0):
    count = start
    def increment():
        nonlocal count
        count += 1
        return count
    def decrement():
        nonlocal count
        count -= 1
        return count

    return increment,decrement

increment, decrement = make_counter(10)
print(increment()) # Output: 11
print(decrement()) # Output: 10
