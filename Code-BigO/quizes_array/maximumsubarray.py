
#Given an integer array nums, find the subarray with the largest sum, and return its sum.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_current = nums[0]
        max_global = nums[0]
        i = 1
        while(i <= len(nums)-1):
            max_current = max(nums[i],max_current + nums[i])
            max_global = max(max_global,max_current)
            i = i + 1
        return max_global

        