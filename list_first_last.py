li = [2,6,7,8,2]

def same_first_last(nums):
  if len(nums)> 1 and nums[0] == nums[-1]:
    return True
  else:
    return False
print(same_first_last([2,6,7,8,2]))