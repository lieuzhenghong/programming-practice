'''
88. Merge Sorted Array
Easy

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

 

Constraints:

    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1.length == m + n
    nums2.length == n

Accepted
672,593
Submissions
1,691,974
'''

# Friday 2nd October 2110
# Solved 2128 with 2 WAs. Should have been more careful with tracing
# (algo was correct but didn't check edge case)


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Idea: keep two pointers that represent the current selected element of each array,
        # and another pointer that
        # Invariant: always put the larger element into the array
        while n:
            end = m + n - 1
            if not m or nums2[n-1] > nums1[m-1]:
                nums1[end] = nums2[n-1]
                n -= 1
            else:
                nums1[end] = nums1[m-1]
                m -= 1


'''
Trace
[1,2,3,4,5,6*,0,0,0*]
[2,5,6*]

[1,2,3,4,5*,6,0,0*,6]
[2,5,6*]

[1,2,3,4,5*,6,0*,6,6]
[2,5*,6]

[1,2,3,4*,5,6*,5,6,6]
[2,5*, 6]

[1,2,3,4*,5*,5,5,6,6]
[2*,5,6]

[1,2,3*,4*,4,5,5,6,6]
[2*,5,6]

[1,2*,3*,3,4,5,5,6,6]
[2*,5,6]

[1,2**,2,3,4,5,5,6,6]
[*2,5,6]
'''
