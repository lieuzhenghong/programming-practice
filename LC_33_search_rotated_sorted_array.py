'''
# LC 33. Search in Rotated Sorted Array
Medium

Given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You should search for target in nums and if you found return its index, otherwise return -1.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

Attempted solve at September 3rd 2020, 17:12. Found solution at 17:20.
Then pomo ended.

Started up pomo again at 1730 and ended at 1802.
Trying to find the index transformation from non-pivoted array to pivoted array

Then tried again until 1832. Cannot get the find_pivot function correct.
Circle back to this

Used help from 
153. Find Minimum in Rotated Sorted Array. Off by ones KILL me
'''

from typing import List


class Solution:
    def find_pivot(self, nums: List[int]) -> int:
        '''
        Returns the index of the pivot element
        A pivot element a[i]
        must be strictly bigger than the element on the right
        that is, a[i] > a[i+1]

        How do we find the pivot element?
        We start at the middle element.
        If the middle element is the pivot element, we are done.

        If the middle element lies before the pivot element, 
        then nums[mid] > nums[last].
        And the pivot element must lie between the middle element
        and the last element.

        If the middle element lies 

        '''
        l = 0
        r = len(nums) - 1

        '''
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            if nums[1] < nums[0]:
                return 0
            else:
                return 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid+1]:
                # This is the pivot element
                return mid
            elif nums[mid] > nums[-1]:  # Before the pivot
                # If element lies before the pivot,
                # then pivot must lie between mid and end
                l = mid + 1
            else:  # nums[mid] <= nums[-1] # After the pivot
                # If this element lies after the pivot
                r = mid
        '''

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return l

    def unpivot(self, nums: List[int], i: int) -> List[int]:
        # pass
        if len(nums) == 1:
            return nums
        a = nums[i:] + nums[:i]
        return a

    def binary_search(self, nums: List[int], n: int) -> int:
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < n:  # too small
                lo = mid + 1
            elif nums[mid] > n:
                hi = mid
            else:
                return mid
        return -1

    def search(self, nums: List[int], target: int) -> int:
        pivot_point = self.find_pivot(nums)
        sorted_nums = self.unpivot(nums, pivot_point)
        # print(sorted_nums)
        sorted_i = self.binary_search(sorted_nums, target)
        # Then do a simple transformation from sorted i to i
        # The binary search gives you the position in the sorted array
        # And you know exactly where the pivot point is
        # We know the pivot point in the sorted array.
        # print(nums, sorted_nums)

        sorted_pivot_point = len(nums) - pivot_point - 1
        # print(sorted_i)
        if sorted_i == -1:
            return -1
        if sorted_i <= sorted_pivot_point:
            # This element is small and before the pivot element
            # in the sorted list.
            return pivot_point + sorted_i
        else:
            return sorted_i - sorted_pivot_point - 1


def sol(nums, target):
    s = Solution()
    print(nums, target, ': ', s.search(nums, target))


sol([4, 5, 6, 7, 0, 1, 2], 0)  # 4 , 0
sol([4, 5, 6, 7, 0, 1, 2], 3)  # -1
sol([6, 7, 0, 1, 2, 3, 4, 5], 3)  # 3, pivot_elem = 1, +1 = 2, --> 5
sol([6, 7, 0, 1, 2, 3, 4, 5], 6)  # 6, pivot_elem = 1, +1 = 2, --> 0
sol([6, 7, 0, 1, 2, 3, 4, 5], 7)  # 7, 1, --> 1
sol([1], 0)  # -1
sol([1, 3], 1)  # 0
sol([3, 1], 1)  # 1
sol([3, 1], 0)  # -1
sol([3, 1, 2], 1)  # 1
sol([3, 1, 2], 2)  # 2
sol([3, 1, 2], 3)  # 0
sol([2, 3, 1], 3)  # 1
sol([1, 2, 3], 3)  # 2
sol([1, 2, 3], 1)  # 0
sol([2, 3, 4, 5, 1], 1)
