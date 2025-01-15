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
'''
dp implimentation
'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        '''
        ----->s (let i represent s)
        |
        |
        t (let j represent t)
        '''
        dp = [[0]*(len(s)+1) for _ in range(len(t))]
        
        # step 1. write base case
        # which is row wise already initialised as 0
        dp.append([1]*(len(s)+1))
        
        # step 2 -> loop
        # loop must run oposite of recurtion direction
        for i in range(len(t)-1, -1, -1):
            for j in range(len(s)-1, -1, -1):
                # step 3 -> copy paste recurtion
                l, r = 0, 0
                # print(i, j)
                if t[i]==s[j]:
                    l = dp[i+1][j+1]
                r = dp[i][j+1]
                '''the above is not direct copy paste. because i think 
                i have supposed the t in column wise in recurtion but in row wise here'''
                dp[i][j] = l+r
            
        return dp

s = Solution()
# 3
s.numDistinct(s = "rabbbit", t = "rabbit")
# %%
s.numDistinct(s = "babgbag", t = "bag")
# %%
