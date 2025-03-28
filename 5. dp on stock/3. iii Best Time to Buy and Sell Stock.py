'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
- leetcode hard 
n=10^5
so we have to do it in O(n) or O(nlogn) time

- AT most 2 transactions are allowed.

but be afread overthinking that you need to implement #D dp
3D dp doesn't mendatorily mean O(n^3). 
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
# 6
s.maxProfit([3,3,5,0,0,3,1,4])
# %%
# 4
s.maxProfit([1,2,3,4,5])
# %%
'''
this tecnique will not work here.
we may skip any down fall and wait for next bullrun to sell and maximise profit
'''
# 0
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
# continueing after a long period


from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def recurtion(start=0, brought=False, cap=2):
            if cap==0 or start==len(prices):
                return 0# logic: run the loop till the end of list or no more scope to buy.

            if brought:
                # we have 2 choices either to sell or not
                return max(
                    prices[start]+recurtion(start+1, False, cap-1),# sold
                    recurtion(start+1, True, cap)# hold
                )
            else:
                # we have 2 choices either to buy or not
                return max(
                    -prices[start]+recurtion(start+1, True, cap),# bought. buying is not the end of transaction. so cap remains same
                    recurtion(start+1, False, cap)# hold
                )

        return recurtion()

'''
gets ac but not optimal. took almost 2 sec to complete
'''

s = Solution()
# %% dp solution 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        ## setp 1 -> declear dp array
        def recurtion(start=0, brought=False, cap=2):
        - 3 parameters are there. so we can make a 3D dp
        
        so dp[start][brought][cap]
        - `start` goes from 0 to n. 
        - `brought` can be 0 or 1.
        - `cap` can be 0, 1, 2.

        ## step 2 -> set defaule values.
        - befault value is set depending upon `base case`
        - return value is the max profix. which is set to default 0
        - everything else is indicated by index

        ## step 3 -> run loops in oposite direction
        
        ## step 4 -> copy paste logics
        
        ## step 5 -> return value
        start=0, brought=False, cap=2
        '''
        n = len(prices)
        dp = [[[0]*3 for _ in range(2)] for _ in range(n+1)]

        for start in range(n-1, -1, -1):
            for brought in range(2):
                for cap in range(1, 2+1):# during implementation i've noticed for cap we need cap-1. so the loop should run increasing oder
                    # NOTE: we can't start from cap 0. for any cap=0 return would be 0 that is the base case
                    if brought:
                        # we have 2 choices either to sell or not
                        dp[start][brought][cap] = max(
                            prices[start] + dp[start+1][0][cap-1],
                            dp[start+1][1][cap]# hold
                        )
                    else:
                        # we have 2 choices either to buy or not
                        dp[start][brought][cap] = max(
                            -prices[start] + dp[start+1][1][cap],
                            dp[start+1][0][cap]# hold
                        )

        return dp[0][0][2]
'''
ac beats 20%. 1228 ms.
seeing the dp solution it is clear that it is not actually O(n^3)
the inner 2 loops runs in constant time 2*3
so overall time complexity -> O(6n)
'''
s = Solution()
# %% double row obtimisation

class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        bellow = [[0]*3 for _ in range(2)]
        current = [[0]*3 for _ in range(2)]

        for start in range(n-1, -1, -1):
            for brought in range(2):
                for cap in range(1, 2+1):# during implementation i've noticed for cap we need cap-1. so the loop should run increasing oder
                    # NOTE: we can't start from cap 0. for any cap=0 return would be 0 that is the base case
                    if brought:
                        # we have 2 choices either to sell or not
                        current[brought][cap] = max(
                            prices[start] + bellow[0][cap-1],
                            bellow[1][cap]# hold
                        )
                    else:
                        # we have 2 choices either to buy or not
                        current[brought][cap] = max(
                            -prices[start] + bellow[1][cap],
                            bellow[0][cap]# hold
                        )
            bellow = current
            # reset current here. but not needed for now

        return bellow[0][2]
'''
ac beats 27% time: 574ms
'''
s = Solution()
# %% single row obtimisation

class Solution:
    def maxProfit(self, prices) -> int:
        n = len(prices)
        current = [[0]*3 for _ in range(2)]

        for start in range(n-1, -1, -1):
            for brought in range(2):
                for cap in range(1, 2+1):# during implementation i've noticed for cap we need cap-1. so the loop should run increasing oder
                    # NOTE: we can't start from cap 0. for any cap=0 return would be 0 that is the base case
                    if brought:
                        # we have 2 choices either to sell or not
                        current[brought][cap] = max(
                            prices[start] + current[0][cap-1],
                            current[1][cap]# hold
                        )
                    else:
                        # we have 2 choices either to buy or not
                        current[brought][cap] = max(
                            -prices[start] + current[1][cap],
                            current[0][cap]# hold
                        )
            # bellow = current
            # reset current here. but not needed for now

        return current[0][2]

'''
ac beats 27% time: 591ms     -> quite the same as double row implimentation
'''
s = Solution()
s.maxProfit([3,3,5,0,0,3,1,4])
# %%
