# min path sum 4 directions
# we use modified dijkstra

# Imports
import heapq
import math
import numpy as np
import requests

# Get matrix A
file_url = 'https://projecteuler.net/resources/documents/0083_matrix.txt'
lines = requests.get(file_url).text.splitlines()
A = np.array([list(map(int,(line.split(",")))) for line in lines])
rows, cols = len(A), len(A[0])

# Store shortest distance to each node
min_paths = np.array([[math.inf]*cols for _ in range(rows)])
min_paths[0,0] = A[0,0]

# Priority queue: (distance,(row,col))
q = [(min_paths[0,0],(0,0))]
while q:
    
    # Pop cell from the heap
    path, cell = heapq.heappop(q)

    # If we know a shorter path, skip
    if min_paths[cell] < path: continue
    
    # Iterate through neighbors of cell popped from heap
    qr,qc = cell
    for neighbor in [(qr,qc-1),(qr,qc+1),(qr-1,qc),(qr+1,qc)]:

        # Skip nonvalid indices
        r,c = neighbor
        if not (0<=r<rows and 0<=c<cols): continue

        # Distance to cell's neighbor
        neighbor_path = path + A[neighbor]

        # Update if this is the shortest known path to neighbor
        if neighbor_path < min_paths[neighbor]:
            min_paths[neighbor] = neighbor_path
            heapq.heappush(q,(neighbor_path, neighbor))

# The end cell. Farthest from 0,0.
print(min_paths[-1,-1])