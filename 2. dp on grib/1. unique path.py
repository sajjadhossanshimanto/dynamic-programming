'''
counting path proablem

### Recursion pattern
- in the base case you return 0 or 1. usually 1.
    that means for every touch in leaf node we return 1.
- you perform all the recurtion 
    ```
    l = dfs()
     ...
    r = dfs()
    ```
- then return sum of all recurtion. l+ ... +r
    sum of all recursiion represents numbers of subordinate node that touches the leaf.
'''
#%%
from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @lru_cache(None)
        def dfs(x, y):
            if x==m-1 and y==n-1:
                return 1

            if x>=m or y>=n: return 0# out of boundery

            return dfs(x+1, y) + dfs(x, y+1)

        return dfs(0, 0)
'''
time complexity: 2^n
space complexity: O(mn) + O((m-1)+(n-1))
    at max m*n caching + recurtion space
    - for a m*n matrix
    |---------
    | x x x x
    | x x x x
    | x x x x
    our recursion will go 
        - down down down ↓ until end is reached 
        - then we will go → right and down. but no downward cell. so continue to go right and right
    |---------      |---------
    | x x x x       | x x x x
    | ↓ x x x       | ↓ x x x
    | ↓ x x x       | ↓ → → x 
    so at max n-1 downward and m-1 right ward
'''
s = Solution()
# %%
# 28
s.uniquePaths(m = 3, n = 7)
#%%
# 3
s.uniquePaths(m = 3, n = 2)
# %%
'''
dp
clearly it will be a 2D matrix dp
- the base case is n,m cell returns 1
- for writing the (0, 0) recurtion call 1st must finish its
    adjecents (x+1, y) and (x, y+1)
    then summation of them will be written in the current cell
so that means we need to run loops from the buttom
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                if x==m-1 and y==n-1: continue

                # dp[x][y] = dp[x+1][y] + dp[x][y+1] # need some boundery checking
                if x+1>=m:
                    dp[x][y] = dp[x][y+1]
                elif y+1>=n:
                    dp[x][y] = dp[x+1][y]
                else:
                    dp[x][y] = dp[x+1][y] + dp[x][y+1]
        
        return dp[0][0]

# or
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1
        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                if x==m-1 and y==n-1: continue

                right, down = 0, 0
                if x+1<m: down = dp[x+1][y]
                if y+1<n: right = dp[x][y+1]
                dp[x][y] = down + right
        
        return dp[0][0]

#or -> take a extra row & col with value 0

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1
        for x in range(m-1, -1, -1):
            for y in range(n-1, -1, -1):
                if x==m-1 and y==n-1: continue

                dp[x][y] = dp[x+1][y] + dp[x][y+1]
        
        return dp[0][0]


s = Solution()
s.uniquePaths(m = 3, n = 7)
# %%
