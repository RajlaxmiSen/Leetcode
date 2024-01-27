#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^=num
        return result
        # if n == 0:
        #     return False          
        # while n !=1:
        #     if n % 2 != 0 and n != 1:
        #         return False
        #     n = n / 2 
        # return True
        
# @lc code=end

