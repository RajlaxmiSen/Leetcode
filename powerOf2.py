#!/usr/bin/python3
# -*- coding:UTF-8 -*-

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False          
        while n !=1:
            if n % 2 != 0 and n != 1:
                return False
            n = n / 2 
        return True

a = new Solution()
a.isPowerOfTwo(2)
