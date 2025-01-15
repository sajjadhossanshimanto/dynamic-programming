# https://leetcode.com/problems/distinct-subsequences/
#%%
from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # counting leaf problem
        @lru_cache(None)
        def backtrack(i=0, j=0):
            if j==len(t):
                return 1
            if i==len(s): return 0

            l, r = 0, 0
            if s[i]==t[j]:
                l = backtrack(i+1, j+1)
            r = backtrack(i+1, j)
            return l+r
    
        return backtrack()

s = Solution()
# 3
s.numDistinct(s = "rabbbit", t = "rabbit")
# %%
# 5
s.numDistinct(s = "babgbag", t = "bag")
# %%
