#
# @lc app=leetcode id=342 lang=python
#
# [342] Power of Four
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False          
        while n != 1:
            if n % 4 != 0 and n != 1:
                return False
            n = n / 4 
        return True
        
# @lc code=end

