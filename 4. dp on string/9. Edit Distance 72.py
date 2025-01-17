# https://leetcode.com/problems/edit-distance/description/
'''
allowed operations
1. insert any char at any pos
2. remove any char from any pos
3. (special) replace any char by any char

the 3rd option actually makes the question hard
if we have a lcs -> ...r..s.. we need to count intermediate char
as we can perform replace operation here


TODO: what if word2 > word1
'''
#%%
def longestCommonSubsequence(text1: str, text2: str) -> int:
    row, column = len(text1), len(text2)
    dp = [[0]*(column+1) for _ in range(row+1)]

    for i in range(row-1, -1, -1):
        for j in range(column-1, -1, -1):
            if text1[i]==text2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])

    # return dp
    match = []
    i, j = 0, 0
    while i!=row and j!=column:
        if text1[i]==text2[j]:
            match.append((i, j))
            i, j = i+1, j+1
        else:
            if dp[i+1][j]>=dp[i][j+1]:
                i, j = i+1, j
            else:
                i, j = i, j+1
    
    return match

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cummon =  longestCommonSubsequence(word1, word2)
        # left part
        # if cummon[0][0]>cummon[0][1]:
        #     '''
        #     this signifies source word has more char than target word on the left side of their first match
        #     so cummon part will be replaced + removal from source
        #     removal count -> their diff
        #     '''
        #     left = cummon[0][0] - cummon[0][1]
        #     left += cummon[0][0] - left
        # else:
        #     "insertion + replasement"
        left = abs(cummon[0][0] - cummon[0][1])
        left += max(cummon[0][0], cummon[0][1]) - left

        # right part
        right = abs(cummon[-1][0] - cummon[-1][1])
        right += max(cummon[1][0], cummon[-1][1]) - right

        # middle
        # cummon[-1] - cummon[0] + 1
        '''
            cummon[-1][1] - cummon[0][1] + 1 - len(cummon)
        that much char are extra in text2 what does not matches with text1
        - should i rplace or perform remove+insert
        - how much can i replace
        '''
        word2_extra = cummon[-1][1] - cummon[0][1] + 1 - len(cummon)
        word1_extra = cummon[-1][0] - cummon[0][0] + 1 - len(cummon)
        
        # replacement                + insertion
        # min(word1_extra, word2_extra) + abs(word1_extra-word2_extra)
        if word2_extra > word1_extra:
            '''
            word2 -> target word
            target_word has more extra char then
            word1 needs insertion to match word2
            + common part can be replaced
            num of insertion -> is their diff
            '''
            middle = word1_extra + (word2_extra - word1_extra)
        else:
            '''
            source word has less extra char then target so
            word1 needs removal + replacement to match word2
            count of removal -> is their difference
            '''
            # replacement + removal
            middle = word2_extra + (word1_extra-word2_extra)


        return middle
        # return longestCommonSubsequence(word1, word2)
        return left + middle + right

s = Solution()
# %%
# 3
s.minDistance(word1 = "horse", word2 = "ros")
# %%
# 5
s.minDistance(word1 = "intention", word2 = "execution")
# %%
