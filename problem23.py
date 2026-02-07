# Non-Abundant Sums
# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1+2+4+7+14=28, so 28 is a perfect number
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n
# 12 is the smallest abundant number
# all integers greater than 28123 can be written as the sum of two abundant numbers
# However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def d(n):
    # sum of proper divisors. 1 is always divisor.
    s = 1
    # check divisors up to sqrt(n)
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            # add divisor
            s += i
            # add complementary divisor if not square root
            if i != n//i: s += n//i
    return s

# last known number which cannot be written as abundant sums
LIMIT = 28124
# create list of all abundant numbers to LIMIT
abundants = [i for i in range(1,LIMIT) if i < d(i)]
# mark false/true if can be written as sum of abundants
abundant_sum = [False] * LIMIT
# Mark every pair true through sieve
for i in range(len(abundants)):
    for j in range(i,len(abundants)):
        s = abundants[i]+abundants[j]
        if s<LIMIT: abundant_sum[s] = True
        else: break
total = sum(i for i,x in enumerate(abundant_sum) if not x)
print("SUM OF NUMBERS WHICH CANNOT BE EXPRESSED AS SUM OF TWO ABUNDANT NUMBERS:",total)