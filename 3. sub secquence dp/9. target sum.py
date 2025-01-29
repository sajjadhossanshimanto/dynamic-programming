'''
https://leetcode.com/problems/target-sum/

solved from neetcode
https://github.com/sajjadhossanshimanto/leatcode/blob/main/dynamic%20programming/17.%20Target%20Sum%20494.py

after doing all the recurtions the 1st idea that will come to mind
lets run recurtion for all the combination of + and -

yes it is possible but there is a better way
lets say   target = 1-2+3-4+5    then can we say
target = (1+3+5)-(2+4) or
target = s1  -   s2

which we have alread solved
but if we even solve it with our 1st approach it would not be any problem


edges:
- nums[i] can be zeros
'''

