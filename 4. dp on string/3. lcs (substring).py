'''
substring vs sub-sequence
the main difference is 
- substring -> consicutive
- subsequence -> follows oder but not mendatorily have tobe consicutive
'''
#%%
from functools import lru_cache

class Solution:
    def longestCommonSubstring(self, text1: str, text2: str) -> int:

        @lru_cache(None)
        def backtrack(i=0, j=0):
            if i==len(text1) or j==len(text2): return 0

            if text1[i]==text2[j]:
                return 1+backtrack(i+1, j+1)
                # i can't return increamented what ever returned by the function
                # i must check if the returned valure is the value obtained by this consicative iteration
                # there for its hard to do with recurtion
            
            return max(backtrack(i+1, j), backtrack(i, j+1))

        return backtrack()

#%%
'''
code copied from printing lcs
'''

class Solution:
    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        row, column = len(text1), len(text2)
        dp = [[0]*(column+1) for _ in range(row+1)]

        for i in range(row):
            for j in range(column):
                if text1[i]==text2[j]:
                    # just fliped th iteration
                    dp[i][j] = 1 + dp[i-1][j-1]
                # else:
                " if not matched we no need to carry values its adjecents"
                #     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp# max of all value in the dp is the ans
        '''
        now i can iterate seperatedly through all value or
        track a max_cout variable while calculating dp[i][j]
        '''
        
        match = []
        i, j = 0, 0
        while i!=row:
            if text1[i]==text2[j]:
                match.append(text1[i])
                i, j = i+1, j+1# go diagonal
            else:
                # go to the cell with dp[i][j] having max value
                # if both of (i+1, j) (i, j+1) cointains same value we can go to any of them
                if dp[i+1][j]>=dp[i][j+1]:
                    i, j = i+1, j
                else:
                    i, j = i, j+1
        
        return "".join(match)


#%%
s = Solution()
s.longestCommonSubstring(text1 = "abcjklp", text2 = "acjkp" )
# %%
from functools import lru_cache

class Solution:
    def longestCommonSubstring(self, text1: str, text2: str) -> int:
        "tecnique: find max among all node values"

        max_ln = [0]
        @lru_cache(None)
        def backtrack(i=0, j=0):
            if i==len(text1) or j==len(text2): return 0

            if text1[i]==text2[j]:
                ans = 1+backtrack(i+1, j+1)
                max_ln[0] = max(max_ln[0], ans)
                return ans
            
            backtrack(i+1, j)
            backtrack(i, j+1)
            return 0
    
        backtrack()
        return max_ln[0]