'''
https://leetcode.com/problems/partition-equal-subset-sum/


solution from:
    https://github.com/sajjadhossanshimanto/leatcode/blob/main/dynamic%20programming/1D/12.%20416.%20Partition%20Equal%20Subset%20Sum.py
'''
#%%
from typing import List
from functools import lru_cache


#%%
class Solution:
    # tc: 1413 ms
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums)/2
        if half-int(half)>0: return False# if is_float

        @lru_cache(None)# never put lru_cacle(0) 0!=None
        def dfs(start=0, left=int(half)):
            if left==0: return True
            if start>=len(nums): return False
            if left<0: return False

            # pick and non-pick
            if dfs(start+1, left): return True
            if dfs(start+1, left-nums[start]): return True

            return False
        
        return dfs()

s = Solution()
#%%
class Solution:
    # tc: tle
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums)/2
        if half-int(half)>0: return False# if is_float

        @lru_cache(None)
        def dfs(start=0, left=int(half)):
            if left==0: 
                return True
            # if start>=len(nums): return False# auto returned false. as the loop will not 

            for i in range(start, len(nums)):
                '''
                in for loop based implimentations ->
                this checks can also be done after call is made ,
                i mean right bellow the base case statement
                '''
                if nums[i]>left: continue

                if dfs(i+1, left-nums[i]): return True

            return False
        
        return dfs()


s = Solution()
#%%
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        2 paramiters are there start_index & left that can very
        |---------> left
        |
        |
        ↓
        start index

        - `starting index` vering from 0 to len(nums)
        - `left` is vering from half to 0
        - base case is where left=0
        in dp we need to do oposit of original iteration


        '''
        half = sum(nums)/2
        if half-int(half)>0: return False# if is_float

        row, column = len(nums), int(half)
        dp = [[0]*(column+1) for _ in range(row+1)]

        # 1. base case
        for i in dp:
            i[0] = 1# left 0 is true

        # 2. iteration
        for start in range(len(nums)-1, -1, -1):
            for left in range(1, int(half)+1):

                # 3. coppy logic
                for i in range(start, len(nums)):
                    if nums[i]>left: continue

                    dp[start][left] = dp[i+1][left-nums[i]]
                    if dp[start][left]: break
        '''
        3 loops are there what's why getting time errors
        '''

        # start = 0, left=half
        return dp[0][-1]

s = Solution()
#%%
class Solution:
    # tc: 1687ms
    def canPartition(self, nums: List[int]) -> bool:
        '''
        |---------> left
        |
        |
        ↓
        start index

        - `starting index` vering from 0 to len(nums)
        - `left` is vering from half to 0
        '''
        half = sum(nums)/2
        if half-int(half)>0: return False# if is_float
        half = int(half)
        
        row, column = len(nums), int(half)
        dp = [[0]*(column+1) for _ in range(row+1)]
        " extra column -> for base left=0 return true"
        " extra row -> for base start=len(nums) return false"

        # 1. base case
        for i in dp:
            i[0] = 1# left 0 is true
        
        # for j in range(len(dp[0])):
        #     'if start==len(nums): return False'
        #     dp[-1][j] = 0

        for start in range(len(nums)-1, -1, -1):
            for left in range(1, int(half)+1):
                dp[start][left] = dp[start+1][left]
                if left-nums[start]>=0:# so many places to make mistakes
                    dp[start][left] = dp[start][left] or dp[start+1][left-nums[start]]
                '''if dfs(start+1, left): return True
                if dfs(start+1, left-nums[start]): return True'''

        return bool(dp[0][half])
        return dp

s = Solution()
#%%
def target_sum(l, target):
    # tc: 1126ms
    if target-int(target)>0: return False# if float
    target = int(target)

    bellow = [False]*(target+1)
    bellow[0] = True
    curr = [True] + [False]*(target)


    # 2. loops
    for start in range(len(l)-1, -1, -1):
        for left in range(1, target+1):
            pick = bellow[left]

            non_pick = False
            if left-l[start]>=0:
                non_pick = bellow[left-l[start]]
            
            curr[left] = pick or non_pick
        bellow = curr
        curr = [True] + [False]*(target)

    return bellow[-1]
#%% single row obtimisation
def target_sum(l, target):
    if target-int(target)>0: return False# if float
    target = int(target)

    bellow = [False]*(target+1)# this row represents when start==len(nums)
    bellow[0] = True

    for start in range(len(l)-1, -1, -1):
        for left in range(target, 0, -1):# target -> 1
            pick = bellow[left]

            non_pick = False
            if left-l[start]>=0:
                non_pick = bellow[left-l[start]]
            
            bellow[left] = pick or non_pick

    return bellow[-1]

#%% observation 1 on single row obtimisation
def target_sum(l, target):
    # tc: 752 ms with observation 1 only
    # tc: 675ms with both obsrvation
    if target-int(target)>0: return False# if float
    target = int(target)

    bellow = [False]*(target+1)# this row represents when start==len(nums)
    bellow[0] = True

    for start in range(len(l)-1, -1, -1):
        '''
        observation 1: skiping extra iteration
        '''
        for left in range(target, l[start]-1, -1):
            pick = bellow[left]
            non_pick = bellow[left-l[start]]

            bellow[left] = pick or non_pick
            if bellow[-1]: return True
            '''
            observation 2: if by anyhow target is made to need to iterate any more
            '''

    return bellow[-1]

#%%
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        half = sum(nums)/2

        return target_sum(nums, half)

s = Solution()
#%%
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

# s = Solution()
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
# ans: False
s.canPartition(
    [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]
)
# %%
# time limit exceeded
# ans: True
s.canPartition(
    [5,79,2,4,8,16,32,64,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
)
# %%
# false
s.canPartition(
    [100,4,6]
)
# %%
