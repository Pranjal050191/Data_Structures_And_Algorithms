# Given an integer n, return the number of prime numbers that are strictly less than n.

def countPrimes(n: int) -> int:
    if n <= 2:
        return 0
    
    # Boolean array for marking prime numbers
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # Marking multiples of i as False starting from i*i
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    return sum(is_prime)

n = 499979
print(countPrimes(n))


