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

s = Solution()
# %%
# 28
s.uniquePaths(m = 3, n = 7)
#%%
# 3
s.uniquePaths(m = 3, n = 2)
# %%
