def prime_factors(n: int) -> list[int]:
    primefactors = []
    i = 3
    while n%2==0:
        primefactors.append(2)
        n//=2

    while n>1:
        if n%i==0:
            primefactors.append(i)
            n//=i
        else:          
            i+=2

    return primefactors

print(prime_factors(28)) # Output: [2, 2, 7]
