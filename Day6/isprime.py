def is_prime(x):
    if x<=1:
        return False
    if x==2:
        return True
    if x%2==0:
        return False

    for i in range(3,x-1):
        if x%i==0:
            return False

    return True

print(is_prime(3))
print(is_prime(2))
print(is_prime(7))
print(is_prime(8))