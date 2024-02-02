# 10001st Prime
# O(?) Solution

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

def Nth_prime(N):
    prime_ct = 0
    i = 1
    while prime_ct < N:
        i += 1
        if is_prime(i):
            prime_ct += 1
    return prime_ct

print(Nth_prime(10001))