# Largest palindrome product
# O(n^2) solution

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

max_palindrome = 0
for i in range (10,100):
    for j in  range (10,100):
        if is_palindrome(i*j) and max_palindrome < i*j:
            max_palindrome = i*j
print(max_palindrome)