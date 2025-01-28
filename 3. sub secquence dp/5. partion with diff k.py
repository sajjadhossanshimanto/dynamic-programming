'''
# not found in leetcode


if their difference is D then we can say
s1 + s2 = sum(nums)
s1 - s2 = D
-------------------
S1 = [D+sum(nums)]/2

in other words we have to make a target 
-> half + (D/2)
-> half - (D/2) 
so there difference would be in total D


the question may ask for 
-> if exists such subsets (if easy) or
-> the number of subsets (a bit hard)
'''
#%%
from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    bellow = [0]*(k+1)

    # 1. base case
    bellow[0] = 1

    # 2. loops
    for index in range(len(nums)-1, -1, -1):
        for left in range(k, nums[index]-1, -1):
            not_pick = bellow[left]
            pick = bellow[left-nums[index]]
            
            bellow[left] = pick + not_pick
    
    return bellow[k]

def solution(nums, d):
    '''
    2 edge cases:
    - sum(nums)-d has tobe even
    - and greater than zero
    '''
    target = sum(nums)-d
    if target&1 or target<0: return 0
    
    target = target//2
    return subarraySum(nums, target)