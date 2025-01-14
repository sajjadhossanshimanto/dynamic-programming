# https://leetcode.com/problems/longest-common-subsequence/description/

#%%
from itertools import combinations


class Solution:
    '''
    tc: 2^n
    sc: 2^n elements with len max n. so n*2^n
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        for ln in range(len(text1), -1, -1):
            seq = set(map(lambda x:"".join(x), combinations(text1, ln)))
            for sub_seq in combinations(text2, ln):
                if "".join(sub_seq) in seq:
                    return ln
        
        return 0

s = Solution()
# %%
# ans: 3
s.longestCommonSubsequence(text1 = "abcde", text2 = "ace" )
#%%
# ans: 3
s.longestCommonSubsequence(text1 = "abc", text2 = "abc")
#%%
# ans: 0
s.longestCommonSubsequence(text1 = "abc", text2 = "def")
# %%
# memory limit exceeded
# tle
# ans: 6
s.longestCommonSubsequence(text1 = "jgtargjctqvijshexyjcjcre", text2 = "pyzazexujqtsjebcnadahobwf")
# %%
from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(None)
        def backtrack(i=len(text1)-1, j=len(text2)-1):
            if i<0 or j<0: return 0

            if text1[i]==text2[j]:
                return 1+backtrack(i-1, j-1)
            # else
            return max(backtrack(i-1, j), backtrack(i, j-1))
    
        return backtrack()

#%%
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(None)
        def backtrack(i=0, j=0):
            if i==len(text1) or j==len(text2): return 0

            if text1[i]==text2[j]:
                return 1+backtrack(i+1, j+1)
            # else
            return max(backtrack(i+1, j), backtrack(i, j+1))
    
        return backtrack()

s = Solution()
# ans: 4
s.longestCommonSubsequence(text1 = "abcdefghij", text2 = "ecdgi" )
# s.longestCommonSubsequence(text1 = "abcde", text2 = "ace" )
# %%
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row, column = len(text1), len(text2)
        dp = [[0]*(column+1) for _ in range(row+1)]
        # 1. write base case
        # its already written where the last column and row set to zero

        # 2. iterate variables / run loops for inputs
        for i in range(row):
            for j in range(column):
                # 3. 
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + ...# 1 + rest. but the rest is now yet calculated
                else:
                    dp[i][j] = ...


'''
for this reason usually dp is always  oposit of recursion
thats why 
recursion [is called]-> top-down
dp (tabulation) -> buttom up
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row, column = len(text1), len(text2)
        dp = [[0]*(column+1) for _ in range(row+1)]
        # 1. write base case
        # its already written where the last column and row set to zero

        # 2. iterate variables / run loops for inputs
        for i in range(row-1, -1, -1):
            for j in range(column-1, -1, -1):
                # 3. copy paste logics
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        return dp[0][0]

s = Solution()
s.longestCommonSubsequence(text1 = "abcdefghij", text2 = "ecdgi" )
# %%
'''
as there is i+1 and j+1, row obtimisation is possible
'''


class Solution:
    # just takes 323ms
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row, column = len(text1), len(text2)
        bellow = [0]*(column+1)
        curr_row = [0]*(column+1)
        
        for i in range(row-1, -1, -1):
            for j in range(column-1, -1, -1):
                if text1[i]==text2[j]:
                    curr_row[j] = 1 + bellow[j+1]
                else:
                    curr_row[j] = max(bellow[j], curr_row[j+1])
            bellow = curr_row
            curr_row = [0]*(column+1)
        
        return bellow[0]

s = Solution()
s.longestCommonSubsequence(text1 = "abcdefghij", text2 = "ecdgi" )
# %%
# ans: 5
# out: 6
s.longestCommonSubsequence("abcba", "abcbcba")
# %%
'''
further row obtimisation not possible as we need to maintain 2 values from the row bellow
'''