'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

you are allowed to 
- buy and sell stock at any pos but
- can't sell before buying
- we need to do this buy/sell operation only once
return maximum profit

actually the 3rd option makes this question easy.

'''
#%%
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for b in range(len(prices)):
            for s in range(b+1, len(prices)):
                profit = max(profit, prices[s] - prices[b])
        
        return profit
'''
solution gets tle as
tc: n^2 
    n is the len and the len canbe 10^5

so we need to improve it. as it is bluthforce approach 
to improve we are not appling some logic on it.

logic:
for maximum profit -> general sence says 
buy at a lowest price point and sell with a higher price
'''

inf = float("inf")
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = prices[0]
        max_profit = 0

        for i in prices:
            max_profit = max(max_profit, i-min_value)
            min_value = min(min_value, i)
        
        return max_profit

s = Solution()
# 5
s.maxProfit([7,1,5,3,6,4])
# %%
# 0
s.maxProfit([7,6,4,3,1])
#%%
'''
from sliding window: https://github.com/sajjadhossanshimanto/leatcode/blob/main/sliding%20window/11.best%20time%20to%20buy%20and%20sell.py

solution with monotonic stack: monotonic stack at each position
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        ans = 0
        for i in prices:
            profit = 0
            while stack and stack[-1][0] <= i :
                prev = stack.pop()
                profit = max((i - prev[0]) + prev[1], profit)
            ans = max(ans, profit)
            stack.append((i, profit))
        
        return ans

s = Solution()
# %%
'''
10^5 clearly indicates we need to do it in O(n) or O(logn) time complexity

'''