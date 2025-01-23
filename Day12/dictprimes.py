def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(k):
    primes = []
    num = 2
    while len(primes) < k:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Input: k (number of primes to generate)
k = int(input("Enter the value of k (number of primes): "))

# Generate the first k prime numbers
primes = generate_primes(k)

# Create the dictionary using a dictionary comprehension
prime_dict = {n: primes[n-1] for n in range(1, k+1)}

# Output the dictionary
print("Dictionary of n-th primes:", prime_dict)
