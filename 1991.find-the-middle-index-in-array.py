class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        left_sum, right_sum = 0 , 0
        for index , val in enumerate(nums):
            right_sum = total  - left_sum - val
            if right_sum == left_sum:
                return index
            left_sum+=val
        return -1
    
if __name__ == '__main__':

        sol = Solution()
        nums = [2,3,-1,8,4]
        print(sol.twoSum(nums))

        

