# https://leetcode.com/problems/perfect-squares/description/

#%%
from functools import lru_cache


inf = float("inf")
class Solution:
    # ac with worse time complexity of more than 4 sec
    @lru_cache(None)
    def numSquares(self, n: int) -> int:
        if n==0: return 1
        if n<0: return 0

        m = pow(n, .5)
        if m-int(m)==0: return 1

        min_value = inf
        for i in range(int(m), 0, -1):
            min_value = min(min_value, self.numSquares(n-pow(i, 2)))
        
        return min_value+1

s = Solution()
# %%
# 3
s.numSquares(12)
# %%
# 2
s.numSquares(13)
# %%
