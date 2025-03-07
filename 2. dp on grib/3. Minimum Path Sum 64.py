# https://leetcode.com/problems/minimum-path-sum/description/

#%%
from heapq import heappop, heappush
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])

        q = [(grid[0][0], 0, 0)]# cost, x, y
        while q:
            cost, x, y = heappop(q)
            if x==row-1 and y==column-1:
                return cost
            
            for cx, cy in [(x+1, y), (x, y+1)]:
                if cx<0 or cy<0 or cx>=row or cy>=column: continue

                if grid[cx][cy]!=-1: 
                    heappush(q, (cost+grid[cx][cy], cx, cy))
                grid[cx][cy] = -1
'''
- heap push and pop takes log(n) operation where n is the size of heap
- and the looops runs in worse case m*n times

so at max there will be m*n push and pop with m*n iteration
time complexity  : mn*log(mn)
space complexity : O(mn)      for list

m/n <= 200
tc: 4000*log(4000) = 1,84,082 gets tl
                    but 10^7 = 1 sec
'''

s = Solution()
# %%
# ans: 7
s.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])
# %%
# ans: 12
s.minPathSum(grid = [[1,2,3],[4,5,6]])
# %%
# tle
s.minPathSum(
    [[0,7,7,8,1,2,4,3,0,0,5,9,8,3,6,5,1,0],[2,1,1,0,8,1,3,3,9,9,5,8,7,5,7,5,5,8],[9,2,3,1,2,8,1,2,3,7,9,7,9,3,0,0,3,8],[3,9,3,4,8,1,2,6,8,9,3,4,9,4,8,3,6,2],[3,7,4,7,6,5,6,5,8,6,7,3,6,2,2,9,9,3],[2,3,1,1,5,4,7,4,0,7,7,6,9,1,5,5,0,3],[0,8,8,8,4,7,1,0,2,6,1,1,1,6,4,2,7,9],[8,6,6,8,3,3,5,4,6,2,9,8,6,9,6,6,9,2],[6,2,2,8,0,6,1,1,4,5,3,1,7,3,9,3,2,2],[8,9,8,5,3,7,5,9,8,2,8,7,4,4,1,9,2,2],[7,3,3,1,0,9,4,7,2,3,2,6,7,1,7,7,8,1],[4,3,2,2,7,0,1,4,4,4,3,8,6,2,1,2,5,4],[1,9,3,5,4,6,4,3,7,1,0,7,2,4,0,7,8,0],[7,1,4,2,5,9,0,4,1,4,6,6,8,9,7,1,4,3],[9,8,6,8,2,6,5,6,2,8,3,2,8,1,5,4,5,2],[3,7,8,6,3,4,2,3,5,1,7,2,4,6,0,2,5,4],[8,2,1,2,2,6,6,0,7,3,6,4,5,9,4,4,5,7]]
)
# %%
from functools import lru_cache


inf = float("inf")
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])

        @lru_cache(None)
        def dfs(x=0, y=0):
            if x==row-1 and y==column-1: 
                return grid[x][y]
            if x>=row or y>=column:
                return inf
            
            # upward flow - through returns
            right = grid[x][y] + dfs(x, y+1)
            down = grid[x][y] + dfs(x+1, y)
            return min(right, down)
        
        return dfs()

s = Solution()
s.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])
# %%

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])

        # to impliment memoization need to cache cost of each pos
        # whenever any other dfs occurs checks if current cost is begger
        # if begger then do not continue 
        min_cost = [inf]
        def dfs(x=0, y=0, cost=0):
            if x>=row or y>=column:
                return
            
            cost+=grid[x][y]
            if x==row-1 and y==column-1:
                # down-ward flow
                min_cost[0] = min(cost, min_cost[0])
                return 
            
            dfs(x, y+1, cost)
            dfs(x+1, y, cost)
        
        dfs()
        return min_cost[0]

s = Solution()
s.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])
# %%
# dp solution

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])

        dp = [[0]*(column) for _ in range(row)]

        dp[0][0] = grid[0][0]
        for i in range(row):
            for j in range(column):
                if i==0:
                    if j!=0:
                        # for the 1st row excluding the (0,0)
                        dp[i][j] = grid[i][j]+dp[i][j-1]
                elif j==0: 
                    # for the 1st column of every row only one option
                    dp[i][j] = grid[i][j]+dp[i-1][j]
                else:
                    dp[i][j] = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])

        # return dp[-1][-1]
        return dp

s = Solution()
s.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])
# %%

inf = float("inf")
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row, column = len(grid), len(grid[0])

        upper = [inf]*(column)
        upper[0] = grid[0][0]

        for i in range(row):
            for j in range(column):
                if i==0 and j==0: continue
                if j==0:
                    upper[j] = grid[i][j]+upper[j]
                else:
                    upper[j] = min(grid[i][j] + upper[j], grid[i][j] + upper[j-1])

        return upper

s = Solution()
s.minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]])
# %%
s.minPathSum([[1,2],[1,1]])
# %%
