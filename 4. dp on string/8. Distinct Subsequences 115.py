# https://leetcode.com/problems/distinct-subsequences/
#%%
from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        # counting leaf problem
        count = [0]
        def backtrack(i=0, j=0):
            if j==len(t):
                count[0]+=1
                return
            if i==len(s): return 

            if s[i]==t[j]:
                backtrack(i+1, j+1)
            backtrack(i+1, j)
    
        backtrack()
        return count[0]

s = Solution()
# 3
s.numDistinct(s = "rabbbit", t = "rabbit")
# %%
# 5
s.numDistinct(s = "babgbag", t = "bag")
# %%
