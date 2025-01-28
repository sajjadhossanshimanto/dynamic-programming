'''
solved with detailed explanation TODO: must watch
this one is learned from neetcode
https://github.com/sajjadhossanshimanto/leatcode/blob/main/dynamic%20programming/16.518.%20Coin%20Change%20II.py

this question is the same as before just only difference is 
here we can use replacements (allowed to use single element multiple times)
'''
# https://leetcode.com/problems/coin-change-ii/description/

#%%
from typing import List
from functools import lru_cache


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        def dfs(index=0, left=amount):
            if left==0: return 1
            if index==len(coins): return 0

            not_pick = dfs(index+1, left)
            pick = 0
            if coins[index]<=left:
                '''thats the key difference here
                if we decide to take that we again have that option to re-take that same number
                whats why we will not increase the index 
                '''
                pick = dfs(index, left-coins[index])
            
            return pick + not_pick

        return dfs()

s = Solution()
# %%
# 4 -> with replacement
# 1 -> wiout replacement
s.change(amount = 5, coins = [1,2,5])
# %%
# 0
s.change(amount = 3, coins = [2])
# %%
# 1
s.change(amount = 10, coins = [10])
# %%
