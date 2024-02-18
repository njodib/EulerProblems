''' PROJECT EULER -- PROBLEM 399

Goal:
 * Avoid importing modules or packages (as per Recurse Center sample code rules)
 * Ensure program runs in under 60 seconds (runs in 52s on personal computer)

Problem: 
 * Find the 100 000 000th Fibonacci number that is not divisible by a square
 * Give as your answer its last sixteen digits followed by a comma followed by the number in scientific notation (rounded to one digit after the decimal point).
 * The 200th squarefree fibonacci is given as: 1608739584170445,9.7e53
'''

''' GET LAST DIGITS OF F_n '''
# Returns AxB(mod m), where A and B are 2x2 matrices
def matrix_multiply(A,B,m):
    # Standard cross-multiplication for 2x2 matrices, each element has mod m
    return [ [ (A[r][0] *B[0][c] + A[r][1]*B[1][c]) % m for c in range(2) ] for r in range(2) ]

# Return A^n (mod m) through iterative multiplication, A is a 2x2 matrix
def matrix_power(A,n,m):
    if n==0: return [ [1,0], [0,1] ] # I_2 identity matrix
    B = matrix_power(A,n//2,m) 
    C = matrix_multiply(B,B,m)
    if n%2==1: C = matrix_multiply(C,A,m)
    return C

# Finds last k digits of F_n
def fib_last_digits(n,k):
    A = matrix_power([ [0,1], [1,1] ], n, 10**k)
    return A[1][0]

''' GET # DIGITS IN F_n'''
# Finds ln(x). Without the math module, we need to use the taylor series expansion for ln
def ln(x):
    n = 10**8.
    return n*((x**(1/n))-1)

def log(x):
    return ln(x)/ln(10)

# Finds number of digits in F_n, using log function and Binet's formula
def fib_digits(n):
    phi = (1+(5**0.5))/2
    digits = n*log(phi) - log(5**0.5)
    return int(-(-digits//1))

''' GET FIRST DIGITS OF F_n AS DECIMAL'''
# Return a^n as a low decimal number, with the last digits on the right side of the decimal point
def power(a,n):
    # Compare to matrix_power as power through iterative multiplication
    if n == 1: return a
    b = power(a,n//2)
    c = b*b
    if n%2==1: c*=a
    while c > 10*(5**0.5): c /= 10 # ensures that (c / sqrt(5)) is a single digit
    return c

# Use Binet's formula to calculate an approximation of F_n, where only the first digit is on the left of the decimal
def binet(n):
    # This formula may not yield F_n exactly, but can approximate the first digits very well
    phi = (1+(5**0.5))/2
    return power(phi,n) / (5**0.5)

''' FORMAT ANSWER FOR F_n '''
def format_answer(n):
    return '%i,%.1fe%i'%(fib_last_digits(n,16),binet(n),fib_digits(n)-1)

''' GET PRIMES '''
# Round n to first odd number above n
def round_up_odd(n):
    return int(-(-n//1)) //2*2 + 1

# Generates prime numbers
def primes_below(n):
    yield 2
    # Build a sieve of eratosthenes and cycle through all odd numbers from 3 to sqrt(n) 
    sieve = [True]*n
    edge = round_up_odd(n**0.5)
    for i in range(3,edge,2):
        if sieve[i]:
            yield i
            # Cross off odd multiples of i > i^2
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    for i in range(edge,n,2):
        if sieve[i]: yield i

''' GET CYCLE OF p '''
def find_cycle(p,n_max):
    # Find first instance where F_n (mod p) == 0
    # If n > n_max, cycle is too large to be relevant to the problem
    a,b = 1,1
    for n in range(2,n_max):
        if b==0: return n
        a,b = b,(a+b)%p
    return 0

''' SOLVE PROBLEM '''
def squarefree_fib(N):
    print("Generating sieve...")
    size = 3*N//2
    sieve = [True]*(size)  # square free Fibonacci sieve
    
    print("Filling sieve...")
    for p in primes_below(N//6):
        l = p * find_cycle(p, size//p + 1)
        if l: sieve[l-1::l] = [False]*(size//l)

    print("Counting sieve...")
    i = [ind for ind,n in enumerate(sieve) if n][N-1]+1
    
    print("Answer!")
    print(format_answer(i))

squarefree_fib(200)
squarefree_fib(10**8)

''' EXPLANATION:

General definitions:
 * The fibonacci series divided by any number has a repeating cycle of residues
 * Let n be a divisor of the fibonacci series
 * Let a(n) be the first index of the fibonacci series that evenly divides n

Show cycles are p*a(p)
 * We can show a(m*n) = a(m)*a(n)
 * So, we are able to factor any cycle into a(n) = a(p_1**k_1) * a(p_2**k_2) * ...
 * This means composite divisors are super-cycles of their prime components
 * We can find unique cycles by considering values of a(p**k), where p is prime
 * Because we are only finding square values, consider cycles of form a(p**2)
 * According to Wall's conjecture, a(p**2) = p*a(p)

Finding a(p):
 * There are lots of methods for finding the value of a(p), including factorizing p +-1
 * The fastest method I found was simply walking through the fibonacci series and stopping when F_n (mod p) == 0
 * Index value of n is equal to a(p)
 * The cycle of p^2 is given by p*a(p)

Finding Nth squarefree:
 * The fastest method (I've found) is a sieve of all numbers, and crossing off square cycles
 * From here, we count to the Nth 'True' element, it is our index
 * Any use of the inclusion-exclusion principle or other math led to slower times

Algorithm:
 1. Generate a sieve of False values with size (3/2)*N
 2. Let p be a unique prime number between 2 and (1/6)*N
 3. Find the cycle length for p
 4. Mark multiples of p^2 cycle (p*a(p)) as False in the sieve
 5. After all primes are solved, find the index of the 200th 'True' element in the sieve
 6. Format answer as {last 16 digis},{scientific notation}

Questions:
 1. I'm not 100% sure why (3/2)*N is the best fit for sieve size, or why (1/6)*N is the best prime limit,
    but smaller values yield false answers, and larger values require more computing. This is the best
    I've found through trial + error.
'''