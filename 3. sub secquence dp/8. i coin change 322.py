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
    # down stream only
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        min_node = [inf]
        # node counting problem
        @lru_cache(None)
        def dfs(start=0, left=amount, node_count=0):
            if left==0: 
                min_node[0] = min(min_node[0], node_count)
                return
            if start==len(coins): return
            
            dfs(start+1, left, node_count)# not pick 
            if left-coins[start]>=0:
                "replacements are allowed"
                dfs(start, left-coins[start], node_count+1)# pick

        dfs()
        return -1 if min_node[0]==inf else min_node[0]

s = Solution()
# %% up & down stream
inf = float("inf")
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()

        # node counting problem
        @lru_cache(None)
        def dfs(start=0, left=amount):
            if left==0: 
                return 0
            if start==len(coins): return inf
            
            "node count will not increase for not pick"
            not_pick = dfs(start+1, left)
            pick = inf
            if left-coins[start]>=0:
                "replacements are allowed"
                pick = 1 + dfs(start, left-coins[start])# pick
            
            return min(pick, not_pick)

        ans = dfs()
        return -1 if ans==inf else ans

s = Solution()
#%%
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
# memory limit exiced
s.coinChange(
    [3,7,405,436],
    8839
)
# or maximum recurtion dept will excid as recurtion dept is 3000
# %%
