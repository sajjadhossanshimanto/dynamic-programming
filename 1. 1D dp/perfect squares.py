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
from math import isqrt

class Solution:
    # all numbers can be found as the sums of squares. Lagrange proved that all could be found as the sum of four or less
    # so, this should never equal anything larger than four; it's just a matter of finding out when and by how much
    def numSquares(self, n: int) -> int:
        # simple integer arithmatic to avoid floating point issues
        def perfect_square(n: int) -> bool:
            return n == isqrt(n)**2

        # check all numbers between 1 and sqrt(n) to see if square-pair exists
        def brute_double(n: int) -> bool:
            for i in range(1, isqrt(n) + 1):
                if perfect_square(n - i**2):
                    return True
            return False

        # https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
        def legandre_triple(n: int) -> bool:
            while (n % 4 == 0):
                n //= 4
            return (n % 8 != 7)

        # perfect square case
        if perfect_square(n):
            return 1

        # sum of two squares case
        elif brute_double(n):
            return 2

        # equals three case
        elif legandre_triple(n):
            return 3

        # hardest mathematically, but fortunately we don't have to include it
        else:
            return 4