# Even fibonacci number sum
# O(0.6n) solution
n = 4000000
a,b,sum = 1,2,0
while a < n:
    if a%2==0:
        sum += a
    a,b = b,a+b
print(sum)