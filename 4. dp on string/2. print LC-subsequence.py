'''
learn backtracking tecnique in dp
'''
#%%
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row, column = len(text1), len(text2)
        dp = [[0]*(column+1) for _ in range(row+1)]

        for i in range(row-1, -1, -1):
            for j in range(column-1, -1, -1):
                if text1[i]==text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        
        "now simulate backtrack here to figureout the path whichi is our desired output"
        # return dp
        
        match = []
        i, j = 0, 0
        while i!=row:
            if text1[i]==text2[j]:
                match.append(text1[i])
                i, j = i+1, j+1# go diagonal
            else:
                # go to the cell with dp[i][j] having max value
                # if both of (i+1, j) (i, j+1) cointains same value we can go to any of them
                if dp[i+1][j]>=dp[i][j+1]:
                    i, j = i+1, j
                else:
                    i, j = i, j+1
        
        return "".join(match)

s= Solution()
#%%
s.longestCommonSubsequence(text1 = "abcde", text2 = "ace" )
# %%
s.longestCommonSubsequence("abcba", "abcbcba")
# %%
