# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
'''
provided:
 - you can insert any char at any position -> counter as one operation


something to note 
- i can make any str a palindrom
    just str+str[::-1]
so at max using len(str) i can convert any string to palindrom
this is the key point of the question.

but if i want to minimise the number of insertion we need to know 
how many charecter are common among them that we don't have to insert
like;

if we have str="leetcode" str[::-1] = "edocteel"
common string-> .e....de               ed...e
while joining these 2 string we can recuse the cummon part
leetcode + edocteel -> leetcodocteel
                       --e---d---e
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
    def minInsertions(self, s: str) -> int:
        return len(s)-longestCommonSubsequence(s, s[::-1])
'''
                     - this porthion indicate the longest palindromic portion
we well keep the longest palindromic portion intac and for the rest 
we will just add in reverse manner 
'''

s = Solution()
#%%
# 0
s.minInsertions(s = "zzazz")
# %%
# 2
s.minInsertions(s = "mbadm")
# %%
# 5
s.minInsertions("leetcode")
# %%
