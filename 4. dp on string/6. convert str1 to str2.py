# similer question
# https://leetcode.com/problems/word-ladder/
#%%
'''
abcd ->(to) anc
- 1. can delete any char
- 2. can insert any char at any position

actually we can convert any text1 to text2.
delete all char from text1 and insert char according to text2
so with len(text1)+len(text2) operating required

but if we want to minimise we can thing of what char we can keep intact
- if we do not need to touch maximum char out number of ooperation will be auto minisied

what is nothing but the common part among them
'''

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

def Solution(text1, text2) -> int:
    common = longestCommonSubsequence(text1, text2)
    del_op = len(text1) - common
    insert_op = len(text2) - common

    return del_op + insert_op

Solution("abcd", "anc")
# %%
