from collections import deque
from typing import List

class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        visited = set()
        boundary_set = set()
        def bfs(i, j):
            q = deque([(i,j)])
            visited.add((i,j))
            while q:
                ii, jj = q.popleft()
                A[ii][jj] = 2
                for x, y in [(ii+1,jj), (ii-1,jj), (ii,jj+1), (ii,jj-1)]:
                    if (0 <= x < r and 0 <= y < c):
                        if A[x][y] == 0 and (x,y) not in boundary_set:
                            boundary_set.add((ii,jj))
                        if ((x,y) not in visited
                            and A[x][y] == 1):
                            q.append((x,y))
                            visited.add((x,y))

        """
        start a bfs from the first 1 encountered.
        set all cells to 2 and find the boundary
        in that component.
        """
        r, c = len(A), len(A[0])
        for i in range(r):
            for j in range(c):
                if A[i][j] == 1:
                    bfs(i, j)
                    break
            else:
                continue
            break

        count = 0
        boundary = deque(boundary_set)
        visited.clear()
        # expand boundary until you hit the other component
        while boundary:
            for _ in range(len(boundary)):
                i, j = boundary.popleft()
                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if (0 <= x < r and 0 <= y < c):
                        if A[x][y] == 1:
                            return count
                        elif A[x][y] == 0 and (x,y) not in visited:
                            boundary.append((x,y))   
                            visited.add((x,y))
            count += 1
