# https://leetcode.com/problems/edit-distance/description/
'''
allowed operations
1. insert any char at any pos
2. remove any char from any pos
3. (special) replace any char by any char

the 3rd option actually makes the question hard
if we have a lcs -> ...r..s.. we need to count intermediate char
as we can perform replace operation here
'''
#%%
def longestCommonSubsequence(text1: str, text2: str) -> int:
    row, column = len(text1), len(text2)
    bellow = [0]*(column+1)
    curr_row = [0]*(column+1)
    
    for i in range(row):
        for j in range(column):
            if text1[i]==text2[j]:
                curr_row[j] = 1 + bellow[j-1]
            else:
                curr_row[j] = max(bellow[j], curr_row[j-1])
        bellow = curr_row
        curr_row = [0]*(column+1)

    return bellow[-2]

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cummon =  longestCommonSubsequence(word1, word2)
        remove = len(word1) - cummon
        insert = len(word2) - cummon

        return insert

s = Solution()
# %%
# 3
s.minDistance(word1 = "horse", word2 = "ros")
# %%
# 5
s.minDistance(word1 = "intention", word2 = "execution")