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
                    ''' there are 9 different choises to take '''
                    max_value = max(max_value, backtrack(x+1, cy1, cy2))
            
            if y1==y2:    
                return max_value+grid[x][y1]
            else:
                return max_value + grid[x][y1] + grid[x][y2]

        return backtrack()
'''
time complxity: O(M*N*N) * 9
    - 9 for 9 state
space complexity: O(M*N*N)  for dp array + auxilary space O(n)
    - as at max the the recurtion can occure from the 1st row till last
'''
s = Solution()
# %%
# 24
s.cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]])
# %%
# 28
s.cherryPickup(grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]])
# %%
'''
dp is all about memoization upon recurtion
so to write dp we must have clear idea what our recurtion function is going to return
'''
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])

        # def dfs(x1, x2, y1, y2):# x1 and x2 are same simgle variable would be enough
        dp = [
            [[0]*column for _ in range(column)]
            for _ in range(row)
        ]
        # base case
        for y1 in range(column):
            for y2 in range(column):
                if y1==y2:
                    dp[-1][y1][y2] = grid[-1][y1]
                else:
                    dp[-1][y1][y2] = grid[-1][y1] + grid[-1][y2]

        # return dp

        for x in range(row-2, -1, -1):
            for y1 in range(column):
                for y2 in range(column):
                    max_value = 0
                    for cy1 in (y1+1, y1, y1-1):
                        for cy2 in (y2+1, y2, y2-1):
                            ''' there are 9 different choises to take '''
                            if cy1<0 or cy1>=column or cy2<0 or cy2>=column: continue

                            max_value = max(max_value, dp[x+1][cy1][cy2])
                    
                    if y1==y2:
                        dp[x][y1][y2] = max_value + grid[x][y1]
                    else:
                        dp[x][y1][y2] = max_value + grid[x][y1] + grid[x][y2]
        '''
        we are actually  not computing for just point (0, 0) & (0, -1)
        calculating for every possible combination of starting point y1 & y2
        but just returning the (0,0) & (0,-1) combination results

        so this indeed should have worse time complexity than recursion
        '''
        # return dp[0]

        '''
        dp[x][y1][y2] represents what the sum of dfs if we start from (x, y2) and (x, y1)
        '''
        return dp[0][0][-1]

s = Solution()
s.cherryPickup(grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]])

# %%
