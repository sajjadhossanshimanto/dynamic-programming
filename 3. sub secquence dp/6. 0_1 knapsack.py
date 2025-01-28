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
