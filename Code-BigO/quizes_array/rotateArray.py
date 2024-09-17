#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        calc_list = list()
        k = k % len(nums)
        for y in range(len(nums)-k ,len(nums)):
            print(f'In y loop {nums[y]}')
            calc_list.append(nums[y])
        for i in range(len(nums) - k):
            print(f'In i loop {nums[i]}')
            calc_list.append(nums[i])
        print(f'Printing calc_list {calc_list}')
        nums[:] = calc_list
                                 