# https://leetcode.com/problems/subarray-sum-equals-k/description/
#%%
from typing import List
from functools import lru_cache


# approach for non-negative numbers
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # need tp cpunt how man times leaf is touched
        @lru_cache(None)
        def dfs(index=0, left=k):
            if left==0: 
                return 1
            if index==len(nums): return 0

            not_pick = dfs(index+1, left)
            pick = 0
            if nums[index]<=left:
                pick = dfs(index+1, left-nums[index])
            
            return pick+not_pick
        
        return dfs()

s = Solution()
#%%
'''
one way to trackel zeros.
addition or removal of zeros do not have any changes 
so zeros can be added with all the sub-set counted by dfs
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        while nums[start]==0:
            start+=1
        
        # need tp cpunt how man times leaf is touched
        @lru_cache(None)
        def dfs(index=0, left=k):
            if left==0: 
                return 1
            if index==len(nums): return 0

            not_pick = dfs(index+1, left)
            pick = 0
            if nums[index]<=left:
                pick = dfs(index+1, left-nums[index])
            
            return pick+not_pick
        
        ans = dfs(start)
        return ans*pow(2, start)

s = Solution()

#%%
'''
another way:
we should not stop right after getting left=0 go deeper to the tree. 
'''
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        @lru_cache(None)
        def dfs(index=0, left=k):
            if index==len(nums):
                if left==0: return 1
                return 0

            not_pick = dfs(index+1, left)
            pick = 0
            if nums[index]<=left:
                pick = dfs(index+1, left-nums[index])
            
            return pick+not_pick
        
        return dfs()

s = Solution()
# %%
# 2 -> for contigious
# 3 -> non-contigious
s.subarraySum(nums = [1,1,1], k = 2)
# %%
# 2
s.subarraySum(nums = [1,2,3], k = 3)
# %%
# 1
"surprisingly number can get negative which  is a problem"
s.subarraySum([-1,-1,1], 0)
# %%
"another fault will occure with zero value"
# 4 -> non coontigious => [0, 1], [0, 1], [0,0,1], [1]
# but ours will get us ans: 1
s.subarraySum([0,0,1], 1)
# %%
