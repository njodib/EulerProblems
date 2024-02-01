# Sum Square Difference
# O(1) solution

# Sum square difference of first N natural numbers:
# (1 + 2 + ... + N)^2 - (1^2 + 2^2 + ... + N^2)
#     = ((N/2)(N+1))^2 - (N/6)(N+1)(2N+1)
#     = (N^4 + 2N^3 + N^2)/4 - (2N^3 + 3N^2 + N)/6
#     = (3N^4 + 2N^3 - 3N^2 - 2N)/12

N = 100
diff = (3*(N**4) + 2*(N**3) - 3*(N**2) - 2*N)/12
print(diff)