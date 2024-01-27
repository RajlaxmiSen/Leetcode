#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        store_map = set()
        for num in nums:
            if num in store_map:
                return True
            store_map.add(num)
        return False
        
# @lc code=end

