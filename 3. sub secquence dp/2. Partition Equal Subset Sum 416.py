'''
https://leetcode.com/problems/partition-equal-subset-sum/


solution from:
    https://github.com/sajjadhossanshimanto/leatcode/blob/main/dynamic%20programming/1D/12.%20416.%20Partition%20Equal%20Subset%20Sum.py
'''
#%%
from typing import List


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

# %%
s = Solution()
s.canPartition(
    [1,2,3,5]
)
# %%
