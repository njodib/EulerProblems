# Amicable Numbers
# d(n) is sum of proper divisors of n
# d(220) = 284
#   220: 1,2,4,5,10,11,20,22,44,55,110 -> sum is 284
# d(284) = 220
#   284: 1,2,4,71,142
# Thus 220,284 form an amicable pair and are called amicable numbers
# Evaluate the sum of all the amicable numbers under 10000

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

assert d(284) == 220
assert d(220) == 284

amicable_numbers = set()
for i in range(1, 10000):
    if i == d(d(i)) and i != d(i):
        amicable_numbers.add(i)
        amicable_numbers.add(d(i))
print("amicable numbers under 10000:", amicable_numbers)
print("sum of amicable numbers under 10000:", sum(amicable_numbers))