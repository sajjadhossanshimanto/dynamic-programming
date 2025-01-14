# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#%%
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1, text2 = s, s[::-1]

        row, column = len(text1), len(text2)
        bellow = [0]*(column+1)
        curr_row = [0]*(column+1)
        
        for i in range(row-1, -1, -1):
            for j in range(column-1, -1, -1):
                if text1[i]==text2[j]:
                    curr_row[j] = 1 + bellow[j+1]
                else:
                    curr_row[j] = max(bellow[j], curr_row[j+1])
            bellow = curr_row
            curr_row = [0]*(column+1)
        
        return bellow[0]

s = Solution()
s.longestPalindromeSubseq("bbbab")
# %%
