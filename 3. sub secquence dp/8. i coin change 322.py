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
# %% dp
inf = float("inf")
class Solution:
    # tc: 1116ms
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        '''
        def dfs(start=0, left=amount):
            - dp[start][left]
            - start  ->  will go `0 till len(coin)` [included]
            - amount ->  will go `0 till amount` [included]
        '''
        # 1. dp table 
        dp = [[0]*(amount+1) for _ in range(len(coins)+1)]

        # 2. base case
        "if left==0: return 0"
        # already zros
        "if start==len(coins): return inf"
        for j in range(1, len(dp[0])):
            # from 1 for left==0
            dp[-1][j] = inf

        # 3. loops
        for start in range(len(coins)-1, -1, -1):
            for left in range(amount+1):
                # 4. copy paste logics
                not_pick = dp[start+1][left]
                pick = inf
                if left-coins[start]>=0:
                    pick = 1 + dp[start][left-coins[start]]
                
                dp[start][left] = min(pick, not_pick)

        # 5. ans dp
        ans = dp[0][amount]
        # return ans
        return -1 if ans==inf else ans

s = Solution()
#%%
# dp: row obtimisation
inf = float("inf")
class Solution:
    # tc: 1116ms
    def coinChange(self, coins: List[int], amount: int) -> int:
        # coins.sort()

        bellow = [inf]*(amount+1)
        curr = [0]*(amount+1)

        bellow[0] = 0

        for start in range(len(coins)-1, -1, -1):
            for left in range(amount+1):
                not_pick = bellow[left]
                pick = inf
                if left-coins[start]>=0:
                    pick = 1 + curr[left-coins[start]]
                
                curr[left] = min(pick, not_pick)

            bellow = curr
            curr = [0]*(amount+1)

        # 5. ans dp
        ans = bellow[amount]
        # return ans
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
# 25
s.coinChange(
    [3,7,405,436],
    8839
)
# or maximum recurtion dept will excid as recurtion dept is 3000
# %%
