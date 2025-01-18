'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''
#%%
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]
        for i in range(1, len(prices)):
            if prices[i]>prices[i-1]:
                profit.append(prices[i]-prices[i-1])
        
        return profit

s = Solution()
# %%
s.maxProfit([3,3,5,0,0,3,1,4])
# %%
s.maxProfit([1,2,3,4,5])
# %%
'''
this tecnique will not work here.
we may skip any down fall and wait for next bullrun to sell and maximise profit
'''
s.maxProfit([7,6,4,3,1])
# %%
from heapq import heappush, heappop

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        ans = []
        for i in prices:
            profit = 0
            while stack and stack[-1][0] <= i :
                prev = stack.pop()
                profit = max((i - prev[0]) + prev[1], profit)

            heappush(ans, profit)
            if len(ans)==3:
                heappop(ans)
            stack.append((i, profit))
        
        return ans

s = Solution()
# %%
