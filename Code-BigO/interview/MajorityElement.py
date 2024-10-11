# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
def majorityElement(nums: list[int]) -> int:
    dic = {}
    for i in range(len(nums)):
        if nums[i] in dic:
            value = dic[nums[i]] + 1
            dic[nums[i]] = value
            if (value > int(len(nums)/2)):
                return nums[i]
        else:
            dic[nums[i]] = 1
            value = dic[nums[i]]
            if (value > int(len(nums)/2)):
                return nums[i]


nums = [1]
print(majorityElement(nums))