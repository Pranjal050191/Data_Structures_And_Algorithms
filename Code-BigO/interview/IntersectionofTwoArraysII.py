def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    inter = list()
    for i in range(len(nums1)):
        if nums1[i]  in nums2:
            inter.append(nums1[i])
            nums2.remove(nums1[i])
    return inter

nums1 = [1,2,2,1]
nums2 = [2]
print(intersect(nums1,nums2))


