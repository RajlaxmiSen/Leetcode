#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
            value_index_map = {}
            for i, n in enumerate(nums):
                diff = target - n
                if diff in value_index_map:
                    return [value_index_map[diff] , i]
                value_index_map[n] = i
# @lc code=end

