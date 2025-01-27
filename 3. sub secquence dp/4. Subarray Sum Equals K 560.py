# https://leetcode.com/problems/subarray-sum-equals-k/description/
#%%
from typing import List
from functools import lru_cache

# failed attemp 2
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if k==0: return 0

        # need tp cpunt how man times leaf is touched
        @lru_cache(None)
        def dfs(index=0, left=k):
            if left==0: 
                return 1
            if index==len(nums): return 0

            pick = 0
            if nums[index]<=left:
                pick = dfs(index+1, left-nums[index])
            
            return pick
        
        counter = 0
        for i in range(len(nums)):
            counter+=dfs(i, k)
        
        return counter
        

s = Solution()

# %%
# 2 -> for contigious
# 3 -> non-contigious
s.subarraySum(nums = [1,1,1], k = 2)
# %%
# 2
s.subarraySum(nums = [1,2,3], k = 3)
# %%
s.subarraySum([-1,-1,1], 0)
# %%
