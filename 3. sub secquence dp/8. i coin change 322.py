'''
https://leetcode.com/problems/coin-change/description/

solved from neetcode. good to see but not recomanded
https://github.com/sajjadhossanshimanto/leatcode/blob/main/dynamic%20programming/1D/8.%20322.%20Coin%20Change.py


we will redefine the solution here
'''
#%%
from typing import List
from functools import lru_cache


inf = float("inf")
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        min_node = [inf]
        # node counting problem
        def dfs(start=len(coins)-1, left=amount, node_count=0):
            if left==0: 
                min_node[0] = min(min_node[0], node_count)
                return
            if start==-1: return
            
            dfs(start-1, left, node_count)# not pick 
            if left-coins[start]>=0:
                "replacements are allowed"
                dfs(start, left-coins[start], node_count+1)# pick

        dfs()
        return min_node[0]

s = Solution()
# %%
# 3
s.coinChange(
    coins = [1,2,5], amount = 11
)
# %%
# -1
s.coinChange(
    coins = [2], amount = 3
)
# %%
# 0
s.coinChange(
    coins = [1], amount = 0
)
# %% wa -> 408 may devide given ammount better than 419
# 20
s.coinChange(
    [186,419,83,408],
    6249
)
# %%
