'''
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]



Constraints:

    0 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    nums is a non decreasing array.
    -10^9 <= target <= 10^9

Accepted
562,560
Submissions
1,542,460
'''

# Attempted Thursday 1st October 2020, 1730
# 2 WAs, solved 1805 (35 minutes)
# See comments below

# We'll do a binary search left and a binary search right

'''

Basically an implementation question. Good practice for binary search. It
looks like the binary search solution I memorised actually does work, so I
don't need to memorise another one.

Got stuck with the edge case to find the rightmost element, because the way
my right-binary search works is that it always finds the first non-target
element --- OR, if the rightmost element is the target, it finds the last
target element. So I needed to catch this special case.

I shouldn't have been impatient when I did the trace --- didn't check all
three cases, which would have surfaced the bug without a wrong answer

Runtime: 84 ms, faster than 87.16% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 15.1 MB, less than 64.17% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
'''




from typing import List
class Solution:
    def bSearchLeft(self, nums: List[int], target: int) -> int:
        '''
        Returns the index of the leftmost element in the array
        that equals target, -1 otherwise
        '''
        l = 0
        r = len(nums) - 1
        while (l < r):
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        # At the end of this loop, l == r
        assert(l == r)
        return l if nums[l] == target else -1

    def bSearchRight(self, nums: List[int], target: int) -> int:
        '''
        Returns the index of the rightmost element in the array
        that equals target, -1 otherwise
        '''
        l = 0
        r = len(nums) - 1
        while (l < r):
            mid = (l + r) // 2
            print(l, mid, r)
            if nums[mid] <= target:  # We can keep going to the right
                l = mid + 1
            else:  # nums[mid] > target
                r = mid
        # At the end of this loop, l == r
        assert(l == r)
        # We return l-1 because l gives the index of the first element
        # in the array that is *larger* than target
        # OR, if the last element of the array is the target,
        # it returns the last element of the array
        if nums[l] == target:
            return l
        elif not nums:  # To
            return -1
        else:
            return l-1 if nums[l-1] == target else -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = self.bSearchLeft(nums, target)
        r = self.bSearchRight(nums, target)
        return [l, r]


'''
Let's trace

[-1,0] target -1
    searchLeft:
        l = 0, r = 1,
        while (l < r):
            mid = 0
            mid == target,
                r = mid = 0
        assert(l == r) # True
        nums[l] == 0 hence return l => 0
    searchRight:
        l = 0, r = 1,
        while (l < r):
            mid = 0
            mid == target,
                l = mid+1 = 1
        assert(l == r) # true
        nums[l-1] == 0 == target return l-1 => 0
    return (0, 0)

[-1,0] target 8
    searchLeft:
        l = 0, r = 1,
        while (l < r):
            mid = 0
            nums[mid] < target,
                l = mid+1
                l = 1
        assert(l == r) # True
        nums[l] == 8 != 0 => return -1
    searchRight:
        l = 0, r = 1,
        while (l < r):
            mid = 0
            nums[mid] <= target,
                l = mid+1
        assert(l == r) # true, r = 0
        nums[l-1] == 0 != target => return -1
    return (-1, -1)

[-1,0] target 0

'''


def s(nums: List[int], target: int):
    return (Solution().searchRange(nums, target))


assert(s(nums=[5, 7, 7, 8, 8, 10], target=8) == [3, 4])
assert(s(nums=[5, 7, 7, 8, 8, 10], target=6) == [-1, -1])
assert(s(nums=[2, 2, 3, 4], target=2) == [0, 1])
assert(s(nums=[2, 2, 3], target=2) == [0, 1])
assert(s(nums=[2, 2], target=2) == [0, 1])
assert(s(nums=[2, 2, 2], target=2) == [0, 2])
