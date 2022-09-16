# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    for i, value in enumerate(nums):
        remaining = target - nums[i]
        nums[i] = None
        if remaining in nums:
            return [i, nums.index(remaining)]

nums = [3,2,4]
target = 6
print(twoSum(nums, target))