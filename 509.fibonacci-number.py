#
# @lc app=leetcode id=509 lang=python
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution(object):
   def fib(self, n: int) -> int:
        # formula : f(n) = f(n -1) + f(n-2), f(0) = 0, f(1) = 1
        #brute force
        # a = 0
        # b = 1
        # if n == 0:
        #     return a
        # elif n == 1:
        #     return b
        # else:
        #     for i in range(2, n+1):
        #         c = a+b
        #         a = b 
        #         b = c
        #     return b

        # recursion
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n > 1:
            return Solution.fib(self, n-1) + Solution.fib(self, n-2)

        
# @lc code=end

