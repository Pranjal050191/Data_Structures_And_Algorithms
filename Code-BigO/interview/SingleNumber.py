# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.
def singleNumber(nums: list[int]) -> int:
    set1 = set()
    for i in range(len(nums)):
        if not (nums[i] in set1):
            set1.add(nums[i])
        else:
           set1.remove(nums[i])
    s = set1.pop()
    return s

nums = [4]
print(singleNumber(nums))
