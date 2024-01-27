#
# @lc app=leetcode id=326 lang=python
#
# [326] Power of Three
#

# @lc code=start
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False          
        while n != 1:
            if n % 3 != 0 and n != 1:
                return False
            n = n / 3 
        return True
        
# @lc code=end

