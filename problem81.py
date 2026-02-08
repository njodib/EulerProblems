# Minimum path topleft -> bottomright with only down and right moves

import requests
file_url = 'https://projecteuler.net/resources/documents/0081_matrix.txt'
lines = requests.get(file_url).text.splitlines()

A = [list(map(int,(line.split(",")))) for line in lines]
#A = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(A)
cols = len(A[0])

for diag in range(rows + cols - 3,-1,-1):
    start_r = min(diag, rows - 1)
    end_r = max(0, diag - cols + 1)
    for r in range(start_r, end_r - 1, -1):
        c = diag - r
        if r + 1 < rows and c + 1 < cols: A[r][c] += min(A[r+1][c], A[r][c+1])
        elif r + 1 < rows: A[r][c] += A[r+1][c]
        else: A[r][c] += A[r][c+1]
print(A[0][0])
