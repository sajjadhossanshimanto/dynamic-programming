# https://leetcode.com/problems/wildcard-matching/description/
#%%
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        '''
        p for pattern:
            parttern will only cointain * and ?
            * -> sequence of char of len 0 or more
            ? -> any single char
        '''

        def backtrack(i=0, j=0):
            if i==len(s) and j==len(p):
                return True
            
            if i>=len(s) or j>=len(p):
                return False
            
            if p[j]=="?" or s[i]==p[j]:
                return backtrack(i+1, j+1)
            if p[j]=="*":
                for i in range(i, len(s)+1):
                    if backtrack(i, j+1): return True
            
            return False
        
        return backtrack()

s = Solution()
# %%
s.isMatch("ray", "?ay")
# %%
s.isMatch("abcdef", "ab**ef")
# %%
s.isMatch("abcd", "**abcd")
# %%
# failed test case
s.isMatch("", "***")
# %%
