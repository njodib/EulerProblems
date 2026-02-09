# Minimum path left -> right with only up and down and right moves

import requests
import numpy as np

file_url = 'https://projecteuler.net/resources/documents/0082_matrix.txt'
lines = requests.get(file_url).text.splitlines()

A = [list(map(int,(line.split(",")))) for line in lines]
rows = len(A)
cols = len(A[0])
A = np.array(A)

for col in range(cols-2,-1,-1):
    #print("COLUMN", col)
    min_paths = []

    for row in range(rows):
        min_path = A[row,col]+A[row,col+1]

        # go above
        top_row = row
        while top_row >= 0:
            s = np.sum(A[top_row:row+1,col])
            min_path = min(min_path, s + A[top_row,col+1])
            
            if s < A[row,col+1]: top_row -= 1
            else: break

        # go below
        bottom_row = row+1
        while bottom_row < cols:
            s = np.sum(A[row:bottom_row+1,col])
            min_path = min(min_path, s + A[bottom_row,col+1])

            if s < A[row,col+1]: bottom_row += 1
            else: break

        #print("MIN PATH OF ROW",row,"IS",min_path)
        min_paths.append(min_path)
    
    A[:,col] = min_paths
    #print()

print("MIN PATH SCORE:",min(A[:,0]))