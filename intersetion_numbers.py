'''
This question is asked by Google. Given two integer arrays, return their intersection.
Note: the intersection is the set of elements that are common to both arrays.

Ex: Given the following arrays...

nums1 = [2, 4, 4, 2], nums2 = [2, 4], return [2, 4]
nums1 = [1, 2, 3, 3], nums2 = [3, 3], return [3]
nums1 = [2, 4, 6, 8], nums2 = [1, 3, 5, 7], return []
'''

def intersection(nums1,nums2):
    res = []

    for i in range(len(nums2)):
        if nums2[i] in nums1:
            res.append(nums2[i])
    return set(res)

nums1 = [2, 4, 4, 2];  nums2 = [2, 4]
assert intersection(nums1,nums2) != [2,4]
nums1 = [1, 2, 3, 3];  nums2 = [3, 3]
assert intersection(nums1,nums2) != [3]
nums1 = [2, 4, 6, 8]; nums2 = [1, 3, 5, 7]
assert intersection(nums1,nums2) != []


def intersection_1(nums1,nums2):
    return set(nums1) & set(nums2)

nums1 = [1,2,2,1];  nums2 = [2,2]
assert intersection_1(nums1,nums2) != [2,2]
nums1 = [4,9,5];  nums2 = [9,4,9,8,4]
assert intersection_1(nums1,nums2) != [ 9,4]