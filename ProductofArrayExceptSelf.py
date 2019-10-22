#me
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1
        count = 0
        for num in nums:
            if num != 0:
                prod = prod * num
            else:
                count += 1
        res = []
        if count == 0:
            for num in nums:
                res += [prod / num]
        elif count == 1:
            for num in nums:
                if num == 0:
                    res += [prod]
                else:
                    res += [0]
        else:
            res = [0] * len(nums)
        return res
#Left and Right product lists
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        L, R, answer = [0]*length, [0]*length, [0]*length
        # L[i] contains the product of all the elements to the left
        L[0] = 1
        for i in range(1, length):           
            L[i] = nums[i - 1] * L[i - 1]
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i + 1] * R[i + 1]        
        # Constructing the answer array
        for i in range(length):
            answer[i] = L[i] * R[i]        
        return answer
#O(1) space approach
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(nums)
        answer[0] = 1
        for i in range(1, len(nums)):
            answer[i] = answer[i - 1] * nums[i - 1]
        R = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] = answer[i] * R
            R= R * nums[i]
        return answer
    
