# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

#%%
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(level, brought=False):
            # level -> indicate price day
            # brought -> if true can sell
            if level>=len(prices): 
                return 0
            if (level, brought) in cache:
                return cache[(level, brought)]

            pro = 0 
            pro  = max(pro, dfs(level+1, brought))# cooldown
            if brought:
                pro  = max(pro, dfs(level+2, not brought) + prices[level])# sell
            else:# buying
                pro  = max(pro, dfs(level+1, True) - prices[level])
            
            cache[(level, brought)] = pro
            return pro
        
        return dfs(0)
