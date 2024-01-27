#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        while x > = 0:
            last = x % 10
            rev = rev * 10 + last
            x = x // 10
        
        if rev == x:
            return True

        
# @lc code=end

