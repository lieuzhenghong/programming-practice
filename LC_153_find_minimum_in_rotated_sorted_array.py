'''
153. Find Minimum in Rotated Sorted Array
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example 1:

Input: [3,4,5,1,2] 
Output: 1

Example 2:

Input: [4,5,6,7,0,1,2]
Output: 0

Accepted
484,289
Submissions
1,069,290

# Re-attempted September 20, 2035
Solved 2127. Dirty and hacky solution. 1 WA.
'''

from typing import List

# Initial thoughts; this solution is trivial in O(n) time. Just look through
# the array in one pass.

# Subsequent thoughts: this must be done in O(logn) otherwise the question is trivial.
# How can we tell if an element is minimum?
# An element is the minimum iff:
#  - the element to its left is more than it;
#  - the element to its right is more than it.

# What happens if the element is the leftmost or rightmost?
# Then check the rightmost and leftmost element as well


class Solution:
    def isMinimum(self, nums: List[int], idx: int) -> bool:
        '''
        Returns true iff nums[idx] is the minimum element in the list
        A pretty finicky function and I'm sure there's a way to clean this up
        '''
        if not nums:
            return False
        if len(nums) == 1:
            return True
        if len(nums) == 2:
            return True if min(nums) == nums[idx] else False
        if idx == 0:  # do only the right check
            return (nums[idx] < nums[idx+1] and nums[idx] < nums[len(nums) - 1])
        if idx == len(nums) - 1:
            return (nums[len(nums) - 1] < nums[0] and nums[len(nums) - 1] < nums[len(nums) - 2])
            pass
        else:
            return (nums[idx] < nums[idx-1] and nums[idx] < nums[idx+1])

    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        # print(nums)

        while l <= r:
            mid = (l + r) // 2
            # print(l, mid, r)
            if self.isMinimum(nums, mid):
                return nums[mid]
            elif nums[mid] >= nums[0] and nums[mid] > nums[r]:
                # Two cases
                # If the array has been rotated, then
                # the mid element will be
                # We are still before the minimum element
                # The element must lie between mid (exclusive) and r (incl)
                l = mid + 1
                # But if the array has not been rotated,
                # then nums[mid] <= nums[r]
                # and mid must lie after the minimum element
            else:  # nums[mid] < nums[0]:
                # We are after the minimum element
                # The element must lie between l and mid(exclusive)
                r = mid - 1

            # print(l, mid, r)


def s(nums):
    sol = Solution()
    print(sol.findMin(nums))


s([3, 4, 5, 1, 2])  # 1
s([4, 5, 6, 7, 0, 1, 2])  # 0
s([0, 1])  # 0
s([1, 0])  # 0
s([1])  # 1
s([1, 2, 3])  # 1
