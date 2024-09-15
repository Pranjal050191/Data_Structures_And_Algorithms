class Solution:
    def twoSum(nums, target):
        a = len(nums) - 1
        for x in range(a):
            for y in range(x+1,a):
                print(nums[x],nums[y])
                if (nums[x] + nums[y] == target):
                    return [x,y]
    twoSum([2,7,11,15],9)
