#Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        i = 0
        while (i < len(nums)):
            if  (nums[i] == 0):
                nums.pop(i)
                counter = counter + 1
                if (i != 0):
                    i = i - 1
                else: 
                    i = 0
            else:
                i = i + 1
        for x in range(counter):
            nums.append(0)

        