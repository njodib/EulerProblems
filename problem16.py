# Power Digit Sum
# 2^15=32768, 3+2+7+6+8=26
#  What is the digit sum for 2^1000


# stupid way
# return sum(int(digit) for digit in str(2**1000))

# non-stupid way
def power_digit_sum(n):
    s = [1]
    for _ in range(n):
        s = [x*2 for x in s]
        for i in range(len(s)):
            if s[i] >= 10:
                if i == len(s)-1:
                    s.append(0)
                s[i+1] += s[i]//10
                s[i] = s[i]%10
    return sum(digit for digit in s)

print("POWER DIGIT SUM OF 2**15:", power_digit_sum(15))
print("POWER DIGIT SUM OF 2**1000:", power_digit_sum(1000))