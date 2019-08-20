def twoSum(self, nums, target):
  if len(nums) <= 1:
    return false
  l={}
  for i in range(len(nums)):
    if nums[i] in l:
      return [i, l[nums[i]]]
    else:
      l[target - nums[i]] = i
  
