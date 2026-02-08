# How many different ways can one hundred be written as a sum of at least two positive integers?

# SEE: problem 78

#imports
from itertools import count

# store pentagonal numbers
g = {}
# store integer partitions
p = {0:1}

# iterate n = number of partitions
for n in range (1,101):
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

# note: we subtract p(1) which is single partition, since 100 must a sum of TWO OR MORE integers.
print("p(100)-p(1) =", p[100]-p[1])