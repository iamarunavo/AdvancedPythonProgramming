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


def primegen():
    prime = 2
    while is_prime(prime):
        yield prime
        prime+=1


gen = primegen
for _ in range(10):
    print(next(gen))