# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
def twoSum(nums: list[int], target: int) -> list[int]:
    se = {}
    l = list()
    for i in range(len(nums)):
        if not(nums[i] in se):
            x = target - nums[i]
            se[x] = i
        else:
            l.append(i)
            y = se[nums[i]]
            l.append(y)
    return l
nums = [3,3]
target = 6
print(twoSum(nums,target))

