class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #brute force
        # sorted_nums = sorted(nums)
        # second_last = sorted_nums[-2]
        # last = sorted_nums[-1]
        # max_product = (last - 1) * ( second_last -1 )
        # return max_product
        

        
if __name__ == '__main__':

        sol = Solution()
        nums = [3,4,5,2]
        print(sol.maxProduct(nums))

