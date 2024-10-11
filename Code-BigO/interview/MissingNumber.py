# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

def missingNumber(nums: list[int]) -> int:
    for i in range(len(nums)+1):
        if not (i in nums):
            return i

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))

