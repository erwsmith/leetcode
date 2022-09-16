# Given an integer array nums, return all the triplets 
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

nums = [-1,0,1,2,-1,-4]
output = []
for i in range(len(nums)):
    for j in range(1, len(nums)):
        if j == i:
            break
        for k in range(2, len(nums)):
            if k == i or k == j:
                break
            if nums[i] + nums[j] + nums[k] == 0 and i != j and i != k and j !=k:
                element = [nums[i], nums[j], nums[k]]
                element.sort()
                if element not in output:
                    output.append(element)

print(output)