# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    output = []
    for i in range(len(nums)):
        if i not in output:
            for j in range(1, len(nums)):
                if j != i and j not in output and nums[i] + nums[j] == target:
                    output.append(i)
                    output.append(j)
    return output

nums = [3,2,4]
target = 6
print(twoSum(nums, target))