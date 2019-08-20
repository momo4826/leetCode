#use dictionary
def twoSum(self, nums, target):
  if len(nums) <= 1:
    return false
  d={}
  for i in range(len(nums)):
    if nums[i] in d:
      return [i, d[nums[i]]]
    else:
      d[target - nums[i]] = i
  
