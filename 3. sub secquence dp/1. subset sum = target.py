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
