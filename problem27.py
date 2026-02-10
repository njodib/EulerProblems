from itertools import count

def is_prime(n):
    if n<2: return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

max_primes, best_ab = -1, (0,0)
for a in range(-999,1000):
    for b in range(-1000,1001):
        for n in count(0):
            y = n*n + a*n + b
            if not is_prime(y):
                if n-1 > max_primes:
                    max_primes = n-1
                    best_ab = a,b
                    print(a,b,max_primes)
                break
print(best_ab[0]*best_ab[1])
        