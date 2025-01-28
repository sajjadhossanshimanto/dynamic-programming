# similer question
# https://leetcode.com/problems/subarray-sum-equals-k/description/
#%%
from typing import List
from functools import lru_cache


#%%
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
this will also works with negative
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
'''
To count only `contiguous` subarrays 
recursion is not ideal choise
`prefix sum` is best aplicable here

let solve this for another day
'''

#%%
# dp approach for non-negative numbers
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        def dfs(index=0, left=k):
            index -> can go at max len(num). len(nums) should be accessable
            left -> 0-k. where k is accessable
        |-------> left
        |
        |
        ↓
        index
        '''
        dp = [[0]*(k+1) for _ in range(len(nums)+1)]

        # 1. base case
        "if left==0: return 1"
        for i in dp:
            i[0] = 1
            
        "if index==len(nums): return 0"# already set to zero

        # 2. loops
        for index in range(len(nums)-1, -1, -1):
            for left in range(1, k+1):
                not_pick = dp[index+1][left]
                pick = 0
                if nums[index]<=left:
                    pick = dp[index+1][left-nums[index]]
                
                dp[index][left] = pick + not_pick
                
        return dp
        # return dp[0][k]

s = Solution()
# %%
# row obtimised dp <- double row
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        we observe,
            dp[index+1][left] & dp[index+1][left-nums[index]]
            - current cell value depends upon 2 values both of them are from `index+1` or bellow row
        '''
        bellow = [0]*(k+1)
        curr = [0]*(k+1)

        # 1. base case
        bellow[0] = 1
        curr[0] = 1

        # 2. loops
        for index in range(len(nums)-1, -1, -1):
            for left in range(1, k+1):
                not_pick = bellow[left]
                pick = 0
                if nums[index]<=left:
                    pick = bellow[left-nums[index]]
                curr[left] = pick + not_pick

            bellow = curr
            curr = [1] + [0]*(k)

        return bellow[k]

s = Solution()
# %%
# row obtimised dp <- single row
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        bellow = [0]*(k+1)

        # 1. base case
        bellow[0] = 1

        # 2. loops
        for index in range(len(nums)-1, -1, -1):
            for left in range(k, 0, -1):# k -> 1 
                not_pick = bellow[left]
                pick = 0
                if nums[index]<=left:
                    pick = bellow[left-nums[index]]
                bellow[left] = pick + not_pick
                # this pos -> represents value of the current pos
        return bellow[k]

s = Solution()
# %%
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        bellow = [0]*(k+1)

        # 1. base case
        bellow[0] = 1

        # 2. loops
        for index in range(len(nums)-1, -1, -1):
            for left in range(k, nums[index]-1, -1):# k -> 1 
                not_pick = bellow[left]
                pick = bellow[left-nums[index]]
                "ensured in loop -> left will always greater or equal to nums[index]"
                
                bellow[left] = pick + not_pick
                # this pos -> represents value of the current pos
        return bellow[k]

s = Solution()