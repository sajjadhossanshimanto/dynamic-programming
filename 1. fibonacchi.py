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
