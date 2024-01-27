#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 0 or n == 1:
            return 1
        first = 1
        second = 2
        for _ in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second
        # if n <=1:
        #     return 1
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        
# @lc code=end

