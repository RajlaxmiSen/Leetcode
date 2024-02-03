#
# @lc app=leetcode id=172 lang=python
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution(object):
    @staticmethod
    def trailingZeroes(n):
        """
        :type n: int
        :rtype: int
        """
        # result = 0
        # for i in range(1,n+1):
        #     if i % 5 == 0:
        #         result+=1
        # return result
        result = 0
        while n > 0:
            n //= 5
            result += n
        return result
        #work only for c++ or java
        # for (i=5; i<=5; i=i*5)
        #     result = result + (n/i)

        
# @lc code=end
    
print(Solution.trailingZeroes(5))

