'''
417. Pacific Atlantic Water Flow
Medium

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

    The order of returned grid coordinates does not matter.
    Both m and n are less than 150.



Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).

Started 9th September 2020, 1545
Gave up 1745
'''

# Idea here: make two passes
# First do pacific
# Then do atlantic
# Key recurrence relation: a point is flowable to the ocean
# iff there exists at least one passable direction that is flowable

# In the pacific solution:
# Base case: check if row  = 0  or column = 0
# If yes, mark it in the dictionary as flowable
# If no, check all cardinal directions that are 1) passable and 2) not already visited
# and run recursively

from typing import List, Dict, Tuple


class Solution:

    def getValidAdjacentDirections(self, point, matrix, visited) -> bool:
        x = point[0]  # Row
        y = point[1]  # Column
        directions = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]
        valid_directions = [d for d in directions if
                            d[0] >= 0 and
                            d[1] >= 0 and
                            d[0] < len(matrix) and
                            d[1] < len(matrix[0]) and
                            matrix[d[0]][d[1]] <= matrix[x][y] and
                            tuple(d) not in visited]
        return valid_directions

    def recurse(self, matrix: List[List[int]], point: List[int],
                results: Dict[Tuple[int, int], bool],
                visited: Dict[Tuple[int, int], bool], sink: str) -> bool:

        x = point[0]  # Row
        y = point[1]  # Column
        if sink == "pacific":
            if x == 0 or y == 0:
                results[tuple(point)] = True
                return True
        elif sink == "atlantic":
            if y == len(matrix[0])-1 or x == len(matrix) - 1:
                results[tuple(point)] = True
                return True

        valid_directions = self.getValidAdjacentDirections(
            point, matrix, visited)
        all_passable = []

        # print("Iterating now...")
        for pt in valid_directions:
            # print(f"Looking at point {pt}")
            if tuple(pt) in visited:
                all_passable.append(results[tuple(pt)])
            else:
                visited[tuple(pt)] = True
                passable = self.recurse(matrix, pt, results, visited, sink)
                results[tuple(pt)] = passable
                all_passable.append(passable)
        # print(f"All recurses called on {point}. Result: {any(all_passable)}")
        return any(all_passable)

    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        results_p = {}
        results_a = {}
        results_all = {}
        for x, row in enumerate(matrix):
            for y, col in enumerate(row):
                results_p[tuple([x, y])] = self.recurse(
                    matrix, [x, y], results_p, {}, "pacific")
                results_a[tuple([x, y])] = self.recurse(
                    matrix, [x, y], results_a, {}, "atlantic")
        # print(results_p)
        # print(results_a)
        for key in results_p:
            results_all[key] = results_p[key] and results_a[key]
        return [key for key in results_all if results_all[key] == True]


def s(matrix):
    sol = Solution()
    print(sol.pacificAtlantic(matrix))
    print(len(sol.pacificAtlantic(matrix)))


'''
s([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
s([])
s([[1], [2], [3]])
s([[1, 1], [1, 1], [1, 1]])
'''

s([[3, 3, 3, 3, 3, 3], [3, 0, 3, 3, 0, 3], [3, 3, 3, 3, 3, 3]])

s([[1, 2, 3, 4, 5, 6, 7], [24, 25, 26, 27, 28, 29, 8], [23, 40, 41, 42, 43, 30, 9], [22, 39, 48, 49,
                                                                                     44, 31, 10], [21, 38, 47, 46, 45, 32, 11], [20, 37, 36, 35, 34, 33, 12], [19, 18, 17, 16, 15, 14, 13]])
# length should be 43 but I get 42
