# Summation of Primes

N = 2000000
sum, sieve = 0, [True] * N
for p in range(2, N):
    if sieve[p]:
        sum += p
        for i in range(p**2, N, p):
            sieve[i] = False
print(sum)