'''
Let p(n) = number of ways n coins can be separated into piles.
For example, five coins can be separated into piles exactly seven ways, so p(5)=7.
    1. ooooo
    2. oooo o
    3. ooo oo
    4. ooo o o
    5. oo oo o
    6. oo o o o
    7. o o o o o
Find the least value of n for which p(n) is divisible by 1 million.
'''

# https://en.wikipedia.org/wiki/Integer_partition
# https://en.wikipedia.org/wiki/Pentagonal_number_theorem

#imports
from itertools import count

# store pentagonal numbers
g = {}
# store integer partitions
p = {0:1}

# iterate n = number of partitions
for n in count(1):
    partitions = 0
    # build recurrence relation
    for k in count(1):
        # get pentagonal numbers
        if k in g:
            g1,g2,sign = g[k]
        else: 
            g1 = k * (3 * k - 1) // 2
            g2 = -k * (3 * -k - 1) // 2
            sign = 1 if k%2==1 else -1
            g[k] = g1,g2,sign

        # break if pentagonal numbers exceed n (equivalent to finding negative partition)
        if g1>n and g2>n: break

        # add previous partitions. compute recurrence relation
        if n >= g1: partitions += sign * p[n-g1]
        if n >= g2: partitions += sign * p[n-g2]
    
    # store number of partitions
    p[n] = partitions

    # check if number of partitions divides 1 million
    if partitions % 10**6 == 0:
        print(f"First integer n: {n}")
        print(f"p({n}): {partitions}")
        break
    
