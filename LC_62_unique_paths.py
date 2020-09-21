'''
62. Unique Paths
Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
 

Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:

Input: m = 7, n = 3
Output: 28

Example 4:

Input: m = 3, n = 3
Output: 6

Constraints:

    1 <= m, n <= 100
    It's guaranteed that the answer will be less than or equal to 2 * 109.

'''

# Attempted 21st September 2020 1450
# The key recurrence relation is that the valid paths from square (i,j)
# equals the sum of all the valid paths from square(i+i, j)
# and the sum of the valid paths from square(i, j+1)
# Start from the first square (0,0) and do recursive calls
# Handle the base cases: with only one square, there is one valid path
# Solved first try AC 1507

from typing import Dict, Tuple


class Solution:
    def rec(self, m: int, n: int, i: int, j: int, memo: Dict[Tuple[int, int], int]) -> int:
        # Returns the number of valid paths from the point (i,j)
        # check the base case
        if i == m-1 and j == n-1:
            return 1
        directions = [(1, 0), (0, 1)]
        num_directions = 0
        for direction in directions:
            # Check if it's a valid direction
            x, y = (i+direction[0], j+direction[1])  # ns stands for new_square
            if x < m and y < n:  # is valid direction
                # Check if it's already been memoised
                if (x, y) in memo:
                    num_directions += memo[(x, y)]
                else:
                    memo[(x, y)] = self.rec(m, n, x, y, memo)
                    num_directions += memo[(x, y)]
        return num_directions

    def uniquePaths(self, m: int, n: int) -> int:
        totalPaths = self.rec(m, n, 0, 0, {})
        return totalPaths


def s(m, n):
    solution = Solution()
    print(solution.uniquePaths(m, n))


s(m=3, n=7)  # 28
s(m=1, n=1)  # 1
s(m=1, n=2)  # 1
s(m=3, n=2)  # 3
s(m=7, n=3)  # 28
s(m=3, n=3)  # 6
