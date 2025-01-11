# https://leetcode.com/problems/cherry-pickup-ii/description/

#%%
from typing import List, Optional
from functools import lru_cache


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])

        # def dfs(x1, x2, y1, y2):# x1 and x2 are same simgle variable would be enough
        @lru_cache(None)
        def backtrack(x=0, y1=0, y2=column-1):
            if y1<0 or y1>=column or y2<0 or y2>=column:
                return 0
            
            # base case
            if x==row-1:
                if y1==y2: 
                    return grid[x][y1]
                return grid[x][y1] + grid[x][y2]
            
            max_value = 0
            for cy1 in (y1+1, y1, y1-1):
                for cy2 in (y2+1, y2, y2-1):
                    max_value = max(max_value, backtrack(x+1, cy1, cy2))
            
            if y1==y2:    
                return max_value+grid[x][y1]
            else:
                return max_value + grid[x][y1] + grid[x][y2]

        return backtrack()

s = Solution()
# %%
# 24
s.cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]])
# %%
# 28
s.cherryPickup(grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]])
# %%
