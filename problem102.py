# Determine if a point P is in triangle ABC
# We are given coordinates of each point

'''
Method 1 -- Sum vector angles: 
    1) Find 3 vectors connecting P to each A,B,C
    2) Sum angles between these vectors
    3) If sum is 2pi, then P in ABC. Otherwise, it is not.

    From heron's thm:
    theta_AB = cos^-1( [d(A,P)^2 + d(P,B)^2 - d(A,B)^2] / [2 * d(A,P) * d(P,B)] )
    
    This has weird cos^-1 calculations and is inefficient :(
    It would prob. work on this problem, but not larger datasets.

Method 2 -- Convex hull:
    https://mathworld.wolfram.com/TriangleInterior.html
    https://blackpawn.com/texts/pointinpoly/default.html
    1) Check number of points in convex hull of ABC adjoined with P
    2) If hull has 3 points, then P in triangle. If hull has 4, P not in triangle.

    Express P in terms of vectors A,B,C
    Solving: P = A + uB + vC
    We get:
        u = [(P x C) - (A x C)] / (B x C)
        v = [(P x B) - (A x B)] / (B x C)
        Note x is cross product: e.g. AxB = A_x B_y - B_x A_y
    Then P in triangle if u,v>0 and u+v<1
'''
'''
# Triangle with origin
A = -340,495
B = -153,-910
C = 835,-947

# Triangle without origin
X = -175,41
Y = -421,-714
Z = 574,-645

# Origin is point to find
P = 0,0

print(origin_in_triangle(A,B,C))
print(origin_in_triangle(X,Y,Z))
'''

import requests

def point_in_triangle(A,B,C,P):
    # area is signed so that A,B,C can be freely labelled
    # note: area is determiniant of [x y 1]
    # area is 0.5* (AB)x(AC) with AB = B-A, AC = C-A
    area = 0.5 * ((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]))
    u = 1/(2*area)*(cross(C,A) + (C[1] - A[1])*P[0] + (A[0] - C[0])*P[1])
    v = 1/(2*area)*(cross(A,B) + (A[1] - B[1])*P[0] + (B[0] - A[0])*P[1])
    return u>0 and v>0 and 1-u-v>0

# cross of vectors r,s
def cross(r,s):
    return r[0]*s[1] - s[0]*r[1]

def origin_in_triangle(A,B,C):
    # area is signed so that point labelling is irrelevant
    area = 0.5 * ((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]))
    u = cross(C,A) / (2*area)
    v = cross(A,B) / (2*area)
    return u>=0 and v>=0 and 1-u-v>=0

s = 0
file_url = 'https://projecteuler.net/resources/documents/0102_triangles.txt'
lines = requests.get(file_url).text.splitlines()
for line in lines:
    l = list(map(int,(line.split(","))))
    A,B,C = (l[0], l[1]), (l[2], l[3]), (l[4], l[5])
    if origin_in_triangle(A,B,C): s += 1
print(s)