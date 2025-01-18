# https://leetcode.com/problems/wildcard-matching/description/
#%%
from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        p for pattern:
            parttern will only cointain * and ?
            * -> sequence of char of len 0 or more
            ? -> any single char
        '''

        @lru_cache(None)
        def backtrack(i=0, j=0):
            if i==len(s) and j==len(p):
                return True
            if i==len(s):
                # edge case checking
                for j in range(j, len(p)):
                    if p[j]!="*": return False
                return True
            if j>=len(p): return False
            
            if p[j]=="?" or s[i]==p[j]:
                return backtrack(i+1, j+1)
            if p[j]=="*":
                # for i in range(i, len(s)+1):
                #     if backtrack(i, j+1): return True
                '''same thing in pick and not pick approach
                😯 somehow this performs way much better
                '''
                return backtrack(i+1, j) or backtrack(i, j+1)

            return False
        
        return backtrack()

s = Solution()
# %%
s.isMatch("ray", "?ay")
# %%
s.isMatch("abcdef", "ab**ef")
# %%
s.isMatch("abcd", "**abcd")
#%%
s.isMatch("abcde", "a?c*e")
#%%
s.isMatch("abcde", "a?c*de")
# %%
# failed test case
s.isMatch("", "***")
# %%
# dp solution

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        as i represents s. s will be in the x direction
        |----> p
        |
        |
        s
        '''
        row, column = len(s), len(p)
        dp = [[False]*(column+1) for _ in range(row+1)]

        " base cases "
        # if i==len(s) and j==len(p):
        dp[-1][-1] = True
        # if j>=len(p): return False
        for i in range(row):
            dp[i][-1] = False

        for j in range(column-1, -1, -1):
            if p[j]!="*": break
            dp[-1][j] = True

        for i in range(len(s)-1, -1, -1):
            for j in range(len(p)-1, -1, -1):
                if p[j]=="?" or s[i]==p[j]:
                    dp[i][j] = dp[i+1][j+1]
                elif p[j]=="*":
                    dp[i][j] = dp[i+1][j] or dp[i][j+1]
        
        return dp
        return dp[0][0]

s=Solution()
s.isMatch("ray", "?ay")
# %%
