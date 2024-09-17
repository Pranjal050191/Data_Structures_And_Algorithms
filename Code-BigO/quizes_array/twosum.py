#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        calc_map = {}
        for b in range(len(nums)):
            s = target - nums[b]
            if(s in calc_map):
                return[b,calc_map[s]]
            else:
                calc_map[nums[b]] = b

