# Largest prime factor
# O(sqrt(n)) solution
n =  600851475143
i = 2
while i**2 <= n:
    if n%i == 0:
        n //= i
    else:
        i += 1
print(n)