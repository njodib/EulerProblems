# Factorial Digit Sum
# 10! = 3628800 -> 3+6+2+8+8+0+0=27
# Find sum of digits in number 100!

# Power Digit Sum
# 2^15=32768, 3+2+7+6+8=26
#  What is the digit sum for 2^1000


'''See Problem 16 for similar method'''

# stupid way
# return sum(int(digit) for digit in str(2**1000))

# non-stupid way
def factorial_digit_sum(n):
    s = [1]
    # multiply by each number up to n
    for i in range(1,n+1):
        # initial multiplication
        s = [x*i for x in s]
        # carry
        for i in range(len(s)):
            if s[i] >= 10:
                # add new digit if necessary
                if i == len(s)-1:
                    s.append(0)
                s[i+1] += s[i]//10
                s[i] = s[i]%10
    # final carry
    while s[-1] != 0:
        s.append(s[-1]//10)
        s[-2] = s[-2]%10
    # return digit sum
    return sum(digit for digit in s)

print("DIGIT SUM OF 10!:", factorial_digit_sum(10))
assert factorial_digit_sum(10) == 27
print("DIGIT SUM OF 100!:", factorial_digit_sum(100))