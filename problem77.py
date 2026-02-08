# first natural number whose "prime sums count" is 5000 or greater

# https://walkerdoescode.home.blog/2019/11/05/project-euler-problem-77/
# I took some of the solutions from here. I liked the moving target to avoid estimation issues.

def prime_sieve(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(n**0.5) + 1):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]

def sub_problem(target,n):
    primes = prime_sieve(target)
    ways = [1] + [0]*target
    for p in primes:
        for i in range(p, target+1):
            ways[i]+= ways[i-p]
    for x in range(target+1):
        if(ways[x]>=n):
            return x
    return -1

def p77(n):
    c = 10
    while(True):
        a = sub_problem(c, n)
        if(a!=-1):
            return a
        c*=3

print (p77(5000))

