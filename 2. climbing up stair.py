'''
when ever it asks for 
 - count total no of ways 
 - asking for min or max output
generally in this kind of proablem we need to traverse through all the possible way and then 
counts no of way or choice a min/ max outcome. this kind of questions are solved with recursion

in my word if i can form a decition tree then we can apply recursion
how do we know to form a decition tree?
- if it is seen that we have repeated decitions
- on every step we are taking the same decition again and again
when it will form a tree made of decition path.

forming a decition tree
 - try to form the question as different state in other word index
 - do all the stuff we are allowesd by the question/ 
 - in other word. conststract lead by taking decitions
 - if it is no of way sum all. if min/max find while iterating
 like here we are at a index 0 (0 ........ n) and need to go to index n
 from 0 we have 2 decitions   - jump 1    - jump 2
 again from 1 or 2 we have to - jump 1    - jump 2
 ..... so on and so
                0
        1              2
    1       3      3        4
 ## to sum number of ways we sum all the ways
 left = jump 1
 right = jump 2
 total ways = jump1 + jump2 
'''
'''
or we can  say for n'th start number of was
n = n-1 + n-2    thinking from the back
which is actually fibonaschi 
'''


#%%
# https://leetcode.com/problems/climbing-stairs/description/

# class Solution:
#     def climbStairs(self, n: int, i=0) -> int:
#         if n==0: return 1
#         if n==1: return 1# from zero jump 1 to 1

#         left = self.climbStairs(n-1)
#         right = self.climbStairs(n-2)
#         return let+right

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==0: return 1
        if n==1: return 1

        left = self.climbStairs(n-1)
        right = self.climbStairs(n-2)
        return left + right


#tabulation with space observed
class Solution:
    def climbStairs(self, n: int) -> int:
        prev2 = 1
        prev = 1
        for i in range(2, n+1):
            fibo = prev+prev2
            prev2 = prev
            prev = fibo
        
        return fibo