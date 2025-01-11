# https://leetcode.com/problems/cherry-pickup-ii/description/

#%%
from typing import List, Optional
from collections import deque

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])
        # valid_source = deque([(0, 0), (row-1, column-1)])
        dp = [[0]*column for _ in range(row)]
        dp[0][0] = grid[0][0]
        dp[0][-1] = grid[0][-1]
        
        for x in range(row):
            for y in range(column):
                if not dp[x][y]: continue

                for cx, cy in [(x+1, y), (x+1, y-1), (x+1, y+1)]:
                    if 0<=cx<row and 0<=cy<column:    
                        dp[cx][cy] = max(
                            dp[cx][cy],
                            dp[x][y] + grid[cx][cy]
                        )
        return dp[-1]

s = Solution()
# %%
# 24
s.cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]])
# %%
# 28
s.cherryPickup(grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]])
# %%
