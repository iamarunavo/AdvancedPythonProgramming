def sieve_of_eratosthenes(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    primes = []
    for i in range(n):
        if sieve[i]:
            primes.append(i)


    return primes
print(sieve_of_eratosthenes(120))




'''
Concatenation for lists works the same as extend() . This means that if we did [1,
2, 3] + [4, 5, 6] , we would get the list [1, 2, 3, 4, 5, 6] .
Review of append() vs extend() :
However, we cannot do [1, 2, 3] + 4 . We cannot concatenate an integer to a
list, and we also cannot concatenate lists to strings. Only lists can be concatenated
with other lists via the + operator.
If we do list1 * n , we are concatenating list1 to itself n times.
'''
