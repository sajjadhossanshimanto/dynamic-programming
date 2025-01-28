'''
very very important question
this is the one that will come to mind first if an inverviewer wants to ask from dp


input -> 2 array + max_weight
wt  -> 3   4   5
val -> 30  40  60
my max capacity of taking weight is -> 8
what is the max value i can with max weight 8

1st approach that will come to mind -> lets be greedy
take the most costly items first. but this will not actually work

wt  -> 3   2   5
val -> 30  40  60
max_weight -> 6
if we still 60 with most value left capacity is 6-5=1 nothing more to take
but we can actually better value of 40+30 with wt 3+2

this happens due to lack of uniformaty. values and weight are not uniform

so we have seen max value may come from from items with least value. so there is no certain way
so try out all ways choise the best ooption
'''
#%%
# recursion: downflow only
def solution(wt, value, bag_size):
    max_val = [0]
    def dfs(start=0, pre_sum_val=0, pre_sum_wt=0):
        if pre_sum_wt>bag_size: return
        if start==len(wt):
            max_val[0] = max(max_val[0], pre_sum_val)
            return
        
        dfs(start+1, pre_sum_val, pre_sum_wt)
        dfs(start+1, pre_sum_val+value[start], pre_sum_wt+wt[start])
    
    dfs()
    return max_val[0]

print(solution([3, 2, 5], [30, 40, 60], 6))
# %%
# recurtion: up and down stream
def solution(wt, value, bag_size):

    def dfs(start=0, pre_sum_wt=0):# return max value
        if start==len(wt): return 0

        not_pick = dfs(start+1, pre_sum_wt)
        pick = 0
        if pre_sum_wt+wt[start]<=bag_size:
            pick = dfs(start+1, pre_sum_wt+wt[start])+value[start]

        return max(pick, not_pick)

    return dfs()

print(solution([3, 2, 5], [30, 40, 60], 6))
print(solution([3, 4, 5], [30, 40, 50], 8))
# %%
# dp
def solution(wt, value, bag_size):
    '''
    def dfs(start=0, pre_sum_wt=0):
        - `start` will go -> 0 - len(wt) # both end inclusive
        - `pre_sum_wt` -> 0 - bag_size # both end inclusive
        
        values on dp arra are accessed like dp[start][pre_sum_wt]
    '''
    # 1. dp array
    dp = [[0]*(bag_size+1) for _ in range(len(wt)+1)]

    # 2. base case
    "if start==len(wt): return 0"# already zero

    # 3. loops
    for start in range(len(wt)-1, -1, -1):
        for pre_sum_wt in range(bag_size, -1, -1):
            # 4. copy paste logic
            not_pick = dp[start+1][pre_sum_wt]
            pick = 0
            if pre_sum_wt+wt[start]<=bag_size:
                pick = dp[start+1][pre_sum_wt+wt[start]] + value[start]

            dp[start][pre_sum_wt] = max(pick, not_pick)

    # 5. return logic
    "ans -> def dfs(start=0, pre_sum_wt=0): -> default value which is given to the function"
    return dp[0][0]
#%%
# iteration -> obtimisation
def solution(wt, value, bag_size):
    dp = [[0]*(bag_size+1) for _ in range(len(wt)+1)]

    for start in range(len(wt)-1, -1, -1):
        for pre_sum_wt in range(bag_size-wt[start], -1, -1):
            not_pick = dp[start+1][pre_sum_wt]            
            pick = dp[start+1][pre_sum_wt+wt[start]] + value[start]
            '''
            pick = dp[start+1][pre_sum_wt+wt[start]] + value[start]
            i need to make sure this     pre_sum_wt+wt[start]    this do not exists      bag_size
            '''

            dp[start][pre_sum_wt] = max(pick, not_pick)

    return dp[0][0]
#%%
# row obtimised
def solution(wt, value, bag_size):
    bellow = [0]*(bag_size+1)
    curr = bellow.copy()

    for start in range(len(wt)-1, -1, -1):
        for pre_sum_wt in range(bag_size-wt[start], -1, -1):
            not_pick = bellow[pre_sum_wt]
            pick = bellow[pre_sum_wt+wt[start]] + value[start]

            curr[pre_sum_wt] = max(pick, not_pick)

        bellow = curr
        curr = [0]*(bag_size+1)

    return bellow[0]

# %%
print(solution([3, 2, 5], [30, 40, 60], 6))
print(solution([3, 4, 5], [30, 40, 50], 8))
# %%
