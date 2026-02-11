# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# Assume there are k digits
# Maximum possible sum = k*9^5
# Minimum possible number = 10^(k-1)

# k=6 => 10^(6-1) = 100,000 < 6*9^5 = 354,294
# k=7 => 10^(7-1) = 1,000,000 > 413,343
# We only search numbers with 2 -> 6 digits.

print(sum(n for n in range(10,10**6) if int(n) == sum(int(d)**5 for d in str(n))))
