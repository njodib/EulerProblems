import requests
file_url = 'https://projecteuler.net/resources/documents/0067_triangle.txt'
lines = requests.get(file_url).text.splitlines()

arr = [[int(x) for x in line.split(" ")] for line in lines]
# begin at second to last row
for i in range(len(arr)-2, -1, -1):
    for j in range(len(arr[i])):
    # add max value of adj. numbers in row below
        arr[i][j] += max(arr[i+1][j], arr[i+1][j+1])
#after this, the top will hold max path sum
print("max path sum:", arr[0][0])