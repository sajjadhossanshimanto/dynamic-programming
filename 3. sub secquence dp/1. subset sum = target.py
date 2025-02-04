'''
return true false
is there any subsequence that's sum is equal to the given target

similer question: Partition Equal Subset Sum 416
'''

# instade of usuing include non-include pattern
# followiing the for-loop pattren for generation sub sequence from harshit vai

#%%
target=10
l = [1, 2, 5, 2, 2]

def subset_sum(index=0, left=target):
    if left==0: return True

    for i in range(index, len(l)):
        if l[i]>left: continue

        if subset_sum(i+1, left-l[i]): return True
    
    return False

print(subset_sum())
# %%
'''
convertion to tabulation
1. write the base case
'''
# i colud not find any tabulation without pick and non pick implementation

target = 7
l = [1, 2, 5, 2, 2]

def subset_sum():
    n = len(l)
    
    # Create a DP table where dp[i][j] represents whether it's possible
    # to achieve a sum of j using the first i elements of the list.
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    # Base case: A sum of 0 is always achievable (empty subset)
    for i in range(n + 1):
        dp[i][0] = True
    
    # Fill the table
    for index in range(1, n + 1):
        for left in range(1, target + 1):
            if l[index - 1] <= left:  # Include the current element if it's <= the remaining sum
                dp[index][left] = dp[index - 1][left] or dp[index - 1][left - l[index - 1]]
                #                 non pick            or                      pick
            else:  # Exclude the current element as current element is larger
                dp[index][left] = dp[index - 1][left]
                # so only             nonpick

    return dp[n][target]

print(subset_sum())

# %%
