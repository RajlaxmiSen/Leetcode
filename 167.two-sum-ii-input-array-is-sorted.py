#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        value_index_map = {}
        for i, n in enumerate(numbers, start=1):
            diff = target - n
            if diff in value_index_map:
                return [value_index_map[diff] , i]
            value_index_map[n] = i
        
# @lc code=end

