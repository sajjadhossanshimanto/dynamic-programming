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
