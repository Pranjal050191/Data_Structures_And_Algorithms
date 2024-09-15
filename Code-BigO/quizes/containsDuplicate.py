#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        calc_set = set()
        for item in nums:
            if (item in calc_set):
                return True
            else:
                calc_set.add(item)
        return False


        