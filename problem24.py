'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012 021 102 120 201 210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

# Takes n! to fully permute last n digits.
# Do a fucked-up euler's method to get something like:
# 10**6 = 2*9! + 6*8! + 6*7! + 2*6! + 5*5! + 1*4! + 2*3! + 2*2!
# So, pop digit in index 2 to start
# The remainder rotates between the remaining digits
# Get first digit as coefficient to 8!, so pop from index 6
# etc.
# Eventually, we get the 10**6 permutation

def fact(x):
    if x<=1: return 1
    return x*fact(x-1)

digits = [0,1,2,3,4,5,6,7,8,9]
perm = []
s = 10**6 - 1
for n in range(len(digits)-1,-1,-1):
    f = fact(n)
    perm.append(digits.pop(s//f))
    s = s%f
print("".join(map(str,perm)))

