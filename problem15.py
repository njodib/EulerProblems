# Lattice Paths
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20x20 grid

def paths_through_lattice(m,n):
    lattice = [[0]*(m+1) for _ in range(n+1)]
    lattice[0][0] = 1
    for i in range(m+1):
        for j in range(n+1):
            if i > 0: lattice[i][j] += lattice[i-1][j]
            if j > 0: lattice[i][j] += lattice[i][j-1]
    return lattice[-1][-1]

print("# paths on 2x2:", paths_through_lattice(2,2))
print("# paths on 20x20:", paths_through_lattice(20,20))