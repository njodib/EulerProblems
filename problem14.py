# Longest Collatz Sequence
# The following iterative sequence is defined for the set of positive integers:
#   n -> n/2 (n is even)
#   n -> 3n+1 (n is odd)
#   e.g. 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# Which starting number, under one million, produces the longest chain?

h = {1: 1}
def collatz(n):
    if n in h:
        return h[n]
    if n%2 == 0:
        h[n] = 1 + collatz(n//2)
    else:
        h[n] = 1 + collatz(3*n+1)
    return h[n]
print(max((collatz(i), i) for i in range(1, 1000000))[1])