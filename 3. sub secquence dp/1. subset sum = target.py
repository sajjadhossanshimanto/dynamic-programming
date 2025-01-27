'''
return true false
is there any subsequence that's sum is equal to the given target

just have to print true or false
'''

# instade of usuing include non-include pattern
# followiing the for-loop pattren for generation sub sequence from harshit vai

#%% pick and not-pick
from functools import lru_cache

def target_sum(l, target):
    if target-int(target)>0: return False# if float
    target = int(target)

    @lru_cache(None)
    def dfs(start=0, left = target):
        if left==0: return True
        if start==len(l): return False
        if left<0: return False

        if dfs(start+1, left): return True
        if dfs(start+1, left-l[start]): return True

        return False
    
    return dfs()

print(target_sum([1, 2, 5, 2, 2], 10))
#%% pick and not-pick dp
from functools import lru_cache

def target_sum(l, target):
    if target-int(target)>0: return False# if float
    target = int(target)

    '''
    ------->left
    |
    |
    ↓
    start
    '''
        #            left                   start
    dp = [[False]*(target+1) for _ in range(len(l)+1)]
    # 1. write base case
    for i in dp:
        "if left==0: return True"
        i[0] = True
    
    # already false
    # for j in range(dp[0]):
    #     "if start==len(l): return False"
    #     dp[-1][j] = False

    # 2. loops
    for start in range(len(l)-1, -1, -1):
        for left in range(1, target+1):
            # dp[start][left] = dp[start+1][left] or dp[start+1][left-l[start]]
            pick = dp[start+1][left]
            non_pick = False
            "if left<0: return False"
            if left-l[start]>=0:
                non_pick = dp[start+1][left-l[start]]
            
            dp[start][left] = pick or non_pick
    
    return dp[0][-1]# -1 is 

print(target_sum([1, 2, 5, 2, 2], 10))
print(target_sum([1, 2, 5, 2, 2], 15))
print(target_sum([1, 2, 5, 100], 15))
#%%
from functools import lru_cache

def target_sum(l, target):
    if target-int(target)>0: return False# if float
    target = int(target)

    bellow = [False]*(target+1)
    bellow[0] = True
    curr = [True] + [False]*(target)


    # 2. loops
    for start in range(len(l)-1, -1, -1):
        for left in range(1, target+1):
            pick = bellow[left]

            non_pick = False
            if left-l[start]>=0:
                non_pick = bellow[left-l[start]]
            
            curr[left] = pick or non_pick
        bellow = curr
        curr = [True] + [False]*(target)

    return bellow[-1]

#%%
def target_sum(l, target):
    def subset_sum(index=0, left=target):
        if left==0: return True
        if index==len(l): return False

        for i in range(index, len(l)):
            if l[i]>left: continue

            if subset_sum(i+1, left-l[i]): return True

        return False
    
    return subset_sum()


print(target_sum([1, 2, 5, 2, 2], 10))
# %%