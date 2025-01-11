# https://leetcode.com/problems/minimum-falling-path-sum-ii/description/
'''
- available movement are spacified in a tricky to understand manner
" A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column. "
unlike previous question where you were only allowed to move dialonal
here is no mention that we are only limited to move diagonal or in straight

there we can move any where without the exact upward pos
'''
#%%
from typing import List, Optional

inf = float("inf")
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row, column = len(matrix), len(matrix[0])
        
        prev_row = [inf]*(column+2)
        curr_row = [inf]*(column+2)
        for i in range(column):
            prev_row[i+1] = matrix[0][i]
        
        for x in range(1, row):
            for y in range(column):
                temp = prev_row[y+1]
                prev_row[y+1] = inf
                curr_row[y+1] = matrix[x][y] + min(prev_row)
                prev_row[y+1] = temp

            prev_row = curr_row
            curr_row = [inf]*(column+2)
            

        return min(prev_row)

s = Solution()
# %%
# 13
s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])
# %%
# ans = -192
# out: -67
s.minFallingPathSum([[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]])