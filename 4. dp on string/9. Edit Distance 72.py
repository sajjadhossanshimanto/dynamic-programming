# https://leetcode.com/problems/edit-distance/description/
'''
allowed operations
1. insert any char at any pos
2. remove any char from any pos
3. (special) replace any char by any char

the 3rd option actually makes the question hard
if we have a lcs -> ...r..s.. we need to count intermediate char
as we can perform replace operation here

hard one
'''
#%%
from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # "node counter problem"
        @lru_cache(None)
        def recursion(i=0, j=0):
            if j==len(word2):
                "matched"
                return len(word1) - i
            if i==len(word1):
                # requi insertion operation
                return len(word2) - (j)
            
            # logic
            if word1[i]==word2[j]:
                # no operation needs to perform
                return 0 + recursion(i+1, j+1)
        
            # insertion
            insert = 1 + recursion(i, j+1)# hypothetically one char is inserted matching j
            '''deletion:
            after not matching one char is deleted from source word but we are still looking for j
            '''
            remove = 1 + recursion(i+1, j)
            # replace
            rep = 1 + recursion(i+1, j+1)
            return min(insert, remove, rep)
        
        return recursion()


s = Solution()
# %%
# 3
s.minDistance(word1 = "horse", word2 = "ros")
# %%
# 5
s.minDistance(word1 = "intention", word2 = "execution")
# %%
# dp solution

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        as i represents word1 then x->word1
        |----------> word2
        |
        |
        word1
        '''
        row, column = len(word1), len(word2)
        dp = [[0]*(column+1) for _ in range(row+1)]

        # base caes
        for i in range(len(dp)):
            dp[i][-1] = len(word1) - i
        
        for j in range(len(dp[0])):
            dp[-1][j] = len(word2) - j

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i]==word2[j]:
                    dp[i][j] = 0 + dp[i+1][j+1]
                else:
                    insert = 1 + dp[i][j+1]
                    remove = 1 + dp[i+1][j]
                    rep = 1 + dp[i+1][j+1]
                    dp[i][j] = min(insert, remove, rep)
        
        return dp[0][0]

s = Solution()
s.minDistance(word1 = "horse", word2 = "ros")
# %%