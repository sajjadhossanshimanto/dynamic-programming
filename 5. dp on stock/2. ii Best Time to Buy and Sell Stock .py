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
from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        [start_pos][buy_index]
        buy index = -1 means NONE
        '''
        dp = [[0]*(len(prices)+1) for _ in range(len(prices)+1)]


        for start in range(len(prices)-1, -1, -1):
            for buy_index in range(len(prices)+1):
        
                if buy_index!=len(prices):
                    dp[start][buy_index] = max(
                        0,
                        dp[start+1][-1] + prices[start] - prices[buy_index],
                        dp[start+1][buy_index]
                    )
                else:
                    # buy here or not buy
                    dp[start][buy_index] =  max(
                        0,
                        dp[start+1][start],
                        dp[start+1][buy_index]
                    )
            
        return dp[0][0]

s = Solution()
s.maxProfit(prices = [7,1,5,3,6,4])
'''
3 * 10^4
our current recurtion is 2D so TC: O(n^2)

(3*10^4)^2 -> 9*10^8 -> 10^9 (almost)
so n^2 will not fit here
'''
# %%

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def recursion(start=0, bought=False) -> int:
            if start==len(prices):
                return 0
            
            if bought:
                # sell it here or not sell here
                profit = max(
                    prices[start] + recursion(start+1, False),# sold
                    recursion(start+1, bought)# not sold
                )
            else:
                # buy here or not buy
                profit = max(
                    -prices[start] + recursion(start+1, True),
                    recursion(start+1, bought)
                )

            return profit

        return recursion()

s = Solution()
s.maxProfit(prices = [7,1,5,3,6,4])
# %%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dp[start_index][bought] 
        where bought has only 1 values indicationg yes or no
        '''
        dp = [[0]*(2) for _ in range(len(prices)+1)]

        for start in range(len(prices)-1, -1, -1):
            for bought in range(2):
                if bought:
                    # sell it here or not sell here
                    dp[start][bought] = max(
                        prices[start] + dp[start+1][0],# sold
                        dp[start+1][bought]# not sold
                    )
                else:
                    # buy here or not buy
                    dp[start][bought] = max(
                        -prices[start] + dp[start+1][1],
                        dp[start+1][bought]
                    )

        return dp

s = Solution()
s.maxProfit(prices = [7,1,5,3,6,4])
# %%
'''

stock prices are best represented when we draw graps
7| .(7)
6| \            .(6)
5|  \   (5).   / \
4|   \    / \ /   .(4)
3|    \  /   .(3)
2|     \/
1|      .(1)
 |______________________
0 

here we have advantage that we can predict the fiture.
seeing the future we will decide weighter to buy in previous day or not
as we just have to return the max profit no mattr how we does that

on the 1st day the price is 7 but we see the next moment price is gooing tobe down. so we will not buy
the next day price is 1 but it will be increased the next day. so buy here
next day the price is increased we will hold as per as it increases. but next day it will the decreased so we sell here.

thats that we need to do again and again. buy in less sell in heigh price.
if we follow that trend we will notice that we will have sell in (1->5) (3->6)
thats means in every increasing part of the graph

thus our result is the sum of all increasing part of the graph.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):# as 0'th index does not have any previous price
            if prices[i]>prices[i-1]:
                profit += (prices[i] - prices[i-1])
        
        return profit

#%%
# solution from leetcode 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        total = 0
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right# ensuing left tobe the previous minimum value
            else:
                total += prices[right] - prices[left]
                left = right
        return total