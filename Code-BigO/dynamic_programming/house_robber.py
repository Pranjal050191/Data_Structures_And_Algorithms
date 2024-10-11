# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.
def rob(nums):
    # Step 1: Handle edge cases (e.g., empty list, single house, two houses)
    if not (nums):
        return 'Empty List'
    elif(len(nums) ==1) or (len(nums)==2):
        return max(nums)
    # Step 2: Initialize variables to store results of previous computations
    else:
        max_rob = [0] * len(nums)
        # Step 3: Loop through each house in the array
        # Step 3a: Calculate maximum money if current house is robbed
         # Step 3b: Calculate maximum money if current house is not robbed
        max_rob[0] = nums[0]
        max_rob[1] = max(nums[0],nums[1])
        # print(f'Prnjal prinitg max_rob {max_rob}')
        for i in range(2,len(nums)):
            # print(f'Pranjal: {i}, printing nums: {nums[i]}, printing max_rob {max_rob[i-2]} and -1 index {max_rob[i-1]}')
            max_rob[i] = max(nums[i] + max_rob[i-2], max_rob[i-1])
        return max(max_rob)

nums = [2, 7, 9, 3, 1, 4, 5, 20]
print(rob(nums))