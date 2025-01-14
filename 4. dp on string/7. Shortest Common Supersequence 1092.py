# https://leetcode.com/problems/shortest-common-supersequence/
#%%
'''
a super sequence is a string that consist of all the string s1, s2, s3 ...
for a given string s1, s2 we nned to find minimum super sequence

brute, groot
we can just combine them and we will have super sequence -> brutegroot
but the minimum ans is -> bgruoote
                          b-ru--te
                          -gr-oot-
this part is cummon       --r---t-
to minimise the minimise we need to reuse as much as char possible maintaining the oder
that is nothing but lcs

taking this decition is the easy part. the main hard part isto generate the string
'''
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        row, column = len(str1), len(str2)
        dp = [[0]*(column+1) for _ in range(row+1)]
        
        for i in range(1, row+1):
            for j in range(1, column+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # return dp

        match = []
        i, j = row, column
        while i!=0 and j!=0:
            if str1[i-1]==str2[j-1]:
                match.append(str1[i-1])
                i, j = i-1, j-1# go diagonal
            else:
                # go to the cell with dp[i][j] having max value
                # if both of (i+1, j) (i, j+1) cointains same value we can go to any of them
                if dp[i-1][j]>=dp[i][j-1]:
                    match.append(str1[i-1])
                    i, j = i-1, j
                else:
                    match.append(str2[j-1])
                    i, j = i, j-1
        
        while i>0:
            match.append(str1[i-1])
            i-=1
        
        while j>0:
            match.append(str2[j-1])
            j-=1
        
        return "".join(match[::-1])


s = Solution()
# %%
# "cabac"
s.shortestCommonSupersequence(str1 = "abac", str2 = "cab")
# %%
# bgruoote
s.shortestCommonSupersequence("brute", "groot")
# %%
