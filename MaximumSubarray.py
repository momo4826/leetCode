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
        
#divide and conquer approach
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, l, r):
        if l > r:
            return -2147483647
        m = (l + r) /2 
        leftSum = sumNum = 0
        for i in range(m - 1, l - 1, -1):
            sumNum += nums[i]
            leftSum = max(leftSum, sumNum)
        rightSum = sumNum= 0
        for i in range(m + 1, r + 1):
            sumNum += nums[i]
            rightSum = max(rightSum, sumNum)
        middleMax = leftSum + rightSum + nums[m]
        leftMax = self.helper(nums, l, m - 1)
        rightMax = self.helper(nums, m + 1, r)
        return max(middleMax, leftMax, rightMax)
