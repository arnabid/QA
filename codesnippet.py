# get the number of rows and columns of a 2D matrix A
A = [[1,1,1],
     [1,0,1],
     [1,1,1]]
R, C = len(A), len(A[0])

# create a buffer with the same dimensions as matrix A
ans = [[0] * C for _ in A]

# count the number of neighbors of each cell including the cell itself
for r in range(R):
    for c in range(C):
        nei = 0
        for nr in (r-1, r, r+1):
            for nc in (c-1, c, c+1):
                if 0 <= nr < R and 0 <= nc < C:
                    nei += 1
        ans[r][c] = nei
print (ans)
