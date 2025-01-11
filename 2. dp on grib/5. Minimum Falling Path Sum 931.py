# https://leetcode.com/problems/minimum-falling-path-sum/description/
'''
- 3 valid moves
    (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1)

'''
#%%
from typing import List, Optional

'''
actually this questtion is all about just cummon sence
nothing like complex dp applied here
'''
inf = float("inf")
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, column = len(matrix), len(matrix[0])
        
        prev_row = [inf]*(column+2)
        curr_row = [inf]*(column+2)
        for i in range(column):
            prev_row[i+1] = matrix[0][i]
        
        # return prev_row
        for x in range(1, row):
            for y in range(column):
                curr_row[y+1] = matrix[x][y] + min(
                    prev_row[y+1], # y->y+1
                    prev_row[y], # y-1 -> y-1+1
                    prev_row[y+2], # y+1 -> y+1+1
                )
            # print(curr_row)
            prev_row = curr_row
            curr_row = [inf]*(column+2)
            

        return min(prev_row)

s = Solution()
# %%
# 13
s.minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]])
# %%
