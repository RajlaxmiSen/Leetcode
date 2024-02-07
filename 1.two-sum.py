class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #optimal apporach
        value_index_map = {}
        for i, n in enumerate(nums):
            diff = target - n # diff is the second number need for the target
            if diff in value_index_map:
                return [value_index_map[diff] , i]
            value_index_map[n] = i
        #brute force
        # for i, _ in enumerate(nums):
        #     for j , _ in enumerate(nums, start=1):
        #         if i == j or j >= len(nums) : continue
        #         print( nums[i] , nums[j])
        #         if nums[i] + nums[j] == target:
        #             return [i, j ]


