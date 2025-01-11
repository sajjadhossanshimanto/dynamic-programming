'''
https://leetcode.com/problems/triangle/description/
- is this possible with log(n)
'''
#%%
from typing import List, Optional

inf = float("inf")
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        gx, gy = len(triangle)-1, len(triangle[-1])-1

        ans = [inf]
        def dfs(x=0, y=0, pre_sum=0):
            pre_sum+=triangle[x][y]
            if pre_sum>=ans[0]:
                return # no need tocheck any further

            if x==gx:
                # leaf node. no left & right
                ans[0] = min(ans[0], pre_sum)
            else:
                # chek if left & if right
                dfs(x+1, y, pre_sum)
                if y<gy:
                    # there exist left
                    dfs(x+1, y+1, pre_sum)
                # if y=0:

        dfs(0, 0, 0)
        return ans[0]

s = Solution()
# %%
# ans: 11
s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
# %%
# ans: -10
s.minimumTotal([[-10]])
# %%
# ans: -1
# out: 0
s.minimumTotal([[-1],[2,3],[1,-1,-3]])
# %%

from typing import List, Optional

inf = float("inf")
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        gx, gy = len(triangle), len(triangle[-1])

        upper = [inf]*gy
        upper[0] = triangle[0][0]

        for i in range(1, gx):# as there is only one cell in 1st row which is already covered
            for j in range(i, -1, -1):
                if j==0:
                    upper[j] = upper[j]+triangle[i][j]
                else:
                    upper[j] = min(
                        upper[j]+triangle[i][j], 
                        upper[j-1]+triangle[i][j]
                    )

        return min(upper)

s = Solution()
# %%
s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])
# %%
