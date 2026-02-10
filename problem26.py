# PROBLEM: Find d (in range 1->1000) such that 1/d has longest cycle length

# Iterate through each value of d
max_cycle_length, best_d = 0, -1
for d in range(1,1001):

    # Begin long division. Start with r = "1.00000", moving decimal to avoid issues with floats
    rs = []
    r = 10**6
    while True:

        # Get remainder
        r = r%d

        # End long division at remainder = 0
        if r==0: break

        # If we have previously seen this remainder, it starts a new cycle. Calculate its period.
        if r in rs:
            cycle_length = len(rs) - rs.index(r)

            # Update if this is the longest cycle
            if cycle_length > max_cycle_length:
                max_cycle_length = cycle_length
                d = best_d
            
            # We know cycle. Exit division.
            break

        # Otherwise, simply bring down '0' digit in 1.00000 and repeat
        else:
            rs.append(r)
            r *= 10

# Output solution
print(best_d)


    

