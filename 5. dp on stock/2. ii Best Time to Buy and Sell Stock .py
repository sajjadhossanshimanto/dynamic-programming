'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

can perform multiple buy and sell but
can't buy again berfor sell. so we have to buy sell then buy sell

1. whenever there are `a lot of ways`.
2. we `try all ways`. and 
3. `find the best way`
whenever we say try all ways -> we mean `recurtion`
'''
#%%
from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def recursion(start=0, buy_index=None) -> int:
            if start==len(prices):
                return 0
            
            if buy_index!=None:
                # sell it here or not sell here
                return max(
                    0,
                    recursion(start+1, None) + prices[start] - prices[buy_index],
                    recursion(start+1, buy_index)
                )
            else:
                # buy here or not buy
                return max(
                    0,
                    recursion(start+1, start),
                    recursion(start+1, buy_index)
                )
        
        return recursion()

s = Solution()
# %%
# 7
s.maxProfit(prices = [7,1,5,3,6,4])
# %%
# 4
s.maxProfit(prices = [1,2,3,4,5])
# %%
# 0
s.maxProfit([7,6,4,3,1])
# %%
