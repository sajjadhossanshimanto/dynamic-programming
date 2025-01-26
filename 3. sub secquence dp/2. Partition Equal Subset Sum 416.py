'''
https://leetcode.com/problems/partition-equal-subset-sum/


solution from:
    https://github.com/sajjadhossanshimanto/leatcode/blob/main/dynamic%20programming/1D/12.%20416.%20Partition%20Equal%20Subset%20Sum.py
'''
#%%
from typing import List
from functools import lru_cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums)/2
        if half-int(half)>0: return False# if is_float

        @lru_cache(0)
        def dfs(start=0, left=int(half)):
            if left==0: return True
            if start>=len(nums): return False
            if left<0: return False

            # pick and non-pick
            if dfs(start+1, left): return True
            if dfs(start+1, left-nums[start]): return True

            return False
        
        return dfs()



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums)/2

        'advance dp approach'
        sub_set = set([0])# set used instade of list to avoid dublicates
        for i in nums:
            # for j in iter(sub_set): # RuntimeError: Set changed size during iteration
            for j in list(sub_set):
                sub_set.add(i+j)
                if i+j==half: return True
        return False

s = Solution()
#%%
# 1
s.canPartition(
    [1,5,11,5]
)
# %%
# 0
s = Solution()
s.canPartition(
    [1,2,3,5]
)
# %%
# 0
s.canPartition(
    [1,2,5]
)
# %%
# time limit exceeded
s.canPartition(
    [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]
)
# %%
