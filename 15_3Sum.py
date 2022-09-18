# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    output = []
    for i, value in enumerate(nums):
        target = -nums[i]
        print(target)
        # output.append(twoSum(nums, target))
        # return output

def twoSum(nums, target):
    for k, value in enumerate(nums):
        remaining = target - nums[k]
        nums[k] = None
        if remaining in nums:
            return [k, nums.index(remaining)]

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))