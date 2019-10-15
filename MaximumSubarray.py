class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            for i in range(1, len(nums)):
                nums[i] = max(nums[i], nums[i] + nums[i - 1])
            return max(nums)
