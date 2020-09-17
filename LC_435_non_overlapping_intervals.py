'''
435. Non-overlapping Intervals
Medium

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note:

    You may assume the interval's end point is always bigger than its start point.
    Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.

Attempted 17th September 2020, 1214
Solved 1235, took 20 minutes. First time AC. 
Pretty easy problem. I tried to be more rigorous with my thinking, laying out
the greedy solution.
'''

from typing import List

# Suppose we had sorted intervals

# Input: [[1,2],[2,3],[3,4],[1,3]] -> [1,2], [1,3], [2,3], [3,4]

# An interval I is overlapping with another J (WLOG let I[0] < J[0])
# iff I[1] (the end of the first interval) > J[0] (the start of the first interval)
# The greedy solution comes to mind: you *always* want to remove the interval
# with the later end (I[1] or J[1])

# Proof of correctness
# Idea is that we keep a pointer pointing to the leftmost element of consideration
# Suppose we have an array of sorted intervals A.
# Claim 1: if A[i] does not intersect with A[j], then A[i] does not intersect with all A[j+k] for any k > 0.

# Let's do a sliding window solution.
# While there is an overlap, we do not move the left pointer.
# But if there is no overlap, we move the left pointer to that new element
# because of Claim 1.

# Invariant: l points to the earliest element in the array that may or may not
# overlap with an interval after l.
# Any interval before l is guaranteed not to overlap.


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # First, sort the intervals
        a = sorted(intervals)
        # num_erase is the number of elements we need to erase to ensure
        # the list has no overlapping intervals
        l = num_erase = 0
        for (r, current) in enumerate(a):
            # We always compare to the next element
            if l == r:
                continue
            first = a[l]
            # check if the arrays overlap
            if first[1] > current[0]:  # we have an overlap
                num_erase += 1
                # We move the left pointer to the smaller interval
                # (the one with the smaller end value)
                if first[1] > current[1]:
                    l = r
            # We have no overlap. By Claim 1, no other elements will overlap with a[l].
            # We can therefore remove l from consideration.
            else:
                l = r

        return num_erase


def s(intervals):
    sol = Solution()
    print(sol.eraseOverlapIntervals(intervals))


s([])  # 0
s([[1, 2]])  # 0
s([[1, 2], [2, 3], [3, 4], [1, 3]])  # 1
s([[1, 3], [1, 2], [2, 3], [3, 4]])  # 1
s([[1, 8], [1, 4], [1, 2], [1, 3], [2, 3], [3, 4]])  # 3
