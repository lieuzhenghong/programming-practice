'''
# LC 11. Container With Most Water
Medium

Given n non-negative integers a1, a2, ..., an , where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with
x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In
this case, the max area of water (blue section) the container can contain is
49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Attempted to solve from 1300-1325. 
Hit upon the idea of left and right pointer but could not prove its correctness.

The proof is as follows:

1.  Suppose we have a candidate answer i and j. WLOG let h[j] >= h[i].
2.  Suppose there is a better answer between [i,j].

Claim: If there is a better answer between [i, j], then it must lie between
[i+1, j].

Proof:
If the better answer is between [i, j], then it must lie between either
[i+1, j], [i, j-1], or both.

We attempt a proof of contradiction. Suppose the answer lies between
[i, j-1] but not between [i+1, j]. That means that the best answer
must be (i, N) where i <= N <= j.

But notice here that the area is bounded by h[i] since h[j] >= h[i].
Decreasing [j] will only decrease the total area, even if h[j] increases.
Hence, contradiction. The answer must lie

Corollary: If a better answer exists between the bounds [i, j], 
it will always lie within the bounds obtained by moving the bound with the
lower height inwards. Hence, the two-pointer algorithm always gives the correct
answer.

'''


from typing import List


class Solution:
    def areaBetweenTwoPoints(self, a: List[int], i: int, j: int):
        # Idea here: the area of water between two points a[i] and a[j]
        # where j > i WLOG, is min(j, i) * (j-i)
        if j == i:
            return 0
        return min(a[j], a[i]) * abs(j-i)

    def maxArea(self, height: List[int]) -> int:
        # The goal is to find i and j such that
        # min(j, i) * (j-i) is maximised.
        max_area = 0
        left_pointer = 0
        right_pointer = len(height) - 1
        while left_pointer < right_pointer:
            current_area = self.areaBetweenTwoPoints(
                height, left_pointer, right_pointer)
            max_area = max(max_area, current_area)
            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area
