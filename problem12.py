# Highly Divisible Triangular Number
# Triangle numbers: 1,3,6,10,15,21
# 28 is first triangle number with over 5 divisors
# What is the value of the first triangle number to have over five hundred divisors?

# Generates prime numb

def div_ct(n):
    ct = 0
    # square vs non-square
    ct = 0
    edge = (n**0.5)
    if edge%1==0: ct += 1
    else: edge += 1
    for i in range(1,int(edge)):
        if n%i == 0:
            ct += 2
    return ct
#nth triangle num
def tri(n):
    return int((1+n) * (n/2))

def doit():
    i = 1
    while div_ct(tri(i)) < 500: i+= 1
    return tri(i)

print(doit())
