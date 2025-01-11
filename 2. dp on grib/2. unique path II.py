# https://leetcode.com/problems/unique-paths-ii/

#%%
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        curr = [0]*(n+1)

        # edge case obstical in the end point
        curr[n-1] = 0 if obstacleGrid[-1][-1] else 1
        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                if x==m-1 and y==n-1: continue
                if obstacleGrid[x][y]:
                    curr[y] = 0
                else:
                    curr[y] += curr[y+1]

        return curr[2]

s = Solution()
# %%
s.uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]])
# %%
s.uniquePathsWithObstacles([[0,1],[0,0]])
# %%
# edge case
s.uniquePathsWithObstacles([[0,0],[0,1]])