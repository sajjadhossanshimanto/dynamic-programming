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
# TODO: why the matching is done from ack
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(None)
        def backtrack(i=0, j=0):
            if i>=len(text1) or j>=len(text2): return 0

            if text1[i]==text2[j]:
                return 1+backtrack(i+1, j+1)
            # else
            return max(backtrack(i+1, j), backtrack(i, j+1))
    
        return backtrack()

s = Solution()
s.longestCommonSubsequence(text1 = "abcde", text2 = "ace" )
# s.longestCommonSubsequence(text1 = "abcde", text2 = "ace" )
# %%