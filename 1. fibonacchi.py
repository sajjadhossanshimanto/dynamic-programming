#%%
'''
dynamic programming have 2 approaches.
 - memoization -> 
 - tabulation -> also called buttom-up dp
'''

# basic recursion solution
def fibo(n):
    if n==1: return 1
    if n==0: return 0

    return fibo(n-1)+fibo(n-2)

print(fibo(7))# works ok

#%%
'''
whenever we add caching with recursion it becomes dp
which is called memoization
 - we can use dp `array` or `lru cache`
'''

dp = {}
def fibo(n):
    if n in dp: return dp[n]

    if n==1: return 1
    if n==0: return 0

    dp[n] = fibo(n-1)+fibo(n-2)
    return dp[n]

fibo(7)
'''
Here
 - time complexity:  is linear O(N)
 - space compexity:  O(n) + O(n)
    - for recursion stack O(n)
    - for cache array     O(n)
'''
# %%
