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
'''
Now comes the tabulation
tabulation means approaching the solution from base case and reach the desired point
see the dp solution and try to build tabulation solution
 - for an dp[n] fibo = fibo(n-1) + fibo(n-2)
 - so we can say dp[n] = dp[i-1] + dp[i-2]
 - the loop will start from 2 as the recurring relationship sstarts from 2
'''

dp = [0, 1]
def fibo(n):
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    
    return dp[n]

fibo(7)
'''
time complexity : O(n)
space complexity: single O(n)
 - as there is no use of recursion stack
'''
# %%
'''
to optimise further we need some observations
i    :  0  1  2  3  4  5  6  7
fibo :  0  1  1  2  3  5  8  13

i'th fibo only depends upon i-1 and i-2 // previous and prev2
also there is a relation between prev and prev2
after generating the ith fibo. the i becomes the prev
so 
'''

def fibo(n):
    if n<2: return n# for 0 and 1

    prev2 = 0
    prev = 1
    for i in range(2, n+1):
        f = prev+prev2
        prev2 = prev
        prev = f
    
    return f

fibo(7)
'''
space complexity : O(1)
time complexity : O(n)
'''
# %%
