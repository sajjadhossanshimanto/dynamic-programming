'''
https://leetcode.com/problems/longest-increasing-subsequence/description/
- len(num) = 2500
clear indication of dynamic programming (n^2)

solved from neetcode:
https://github.com/sajjadhossanshimanto/leatcode/blob/main/dynamic%20programming/1D/11.%20300.%20Longest%20Increasing%20Subsequence.py
not recomanded to see. we will re-solve it here


we already have learned to generate sub-sequence.
here also we will do pick and non-pick
just extra we have to check one extra decition before picking
eighter it follows the trend of incresing.
'''
#%%
from typing import List
from functools import lru_cache

inf = float("inf")
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def backtrack(curr=0, previous=0):
            if curr==len(nums):
                return 0
            
            not_pick = backtrack(curr+1, curr)
            pick = 0
            if nums[curr]>nums[previous] or curr==0:
                pick = 1+backtrack(curr+1, curr)
            
            return max(pick, not_pick)\
        
        return backtrack()

s = Solution()
# %%
# 4
s.lengthOfLIS([10,9,2,5,3,7,101,18])
# %%
# 1
s.lengthOfLIS(
    [7,7,7,7,7,7,7]
)
# %%
# ans: 4
s.lengthOfLIS(
    [0,1,0,3,2,3]
)
# %%
# 5
s.lengthOfLIS(
    [1, 2, 3, 4, 5]
)
# %%