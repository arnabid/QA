# problem statement - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/

class Solution:
    def __init__(self):
        self.max_len = 0
        self.table = {}

    def longestIncreasingPath(self, matrix):
        def dfs(x, y, prev):
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] <= prev: return 0
            # print (x,y) - debugging
            if (x,y) in self.table: return self.table[(x,y)]
            path = 1 + max(dfs(x, y+1, matrix[x][y]), dfs(x+1, y, matrix[x][y]), dfs(x, y-1, matrix[x][y]), dfs(x-1, y, matrix[x][y]))
            self.max_len = max(self.max_len, path)
            self.table[(x,y)] = path
            return path

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, -1)
        return self.max_len
