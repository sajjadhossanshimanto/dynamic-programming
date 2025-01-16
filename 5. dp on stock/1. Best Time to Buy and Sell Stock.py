'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
#%%
from typing import List


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
