# Special Pythagorean Triplet
# Find abc such that a^2+b^2=c^2 and a+b+c=1000 and a<b<c

for a in range(1,333):
    for b in range(a+1,1000-a):
        c = 1000-a-b
        if a**2 + b**2 == c**2:
            print(a*b*c)
            exit