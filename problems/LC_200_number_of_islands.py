'''
200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of
islands. An island is surrounded by water and is formed by connecting
adjacent lands horizontally or vertically. You may assume all four edges of
the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''
from typing import List

# If I keep the idea of a "root node", and DFS from there while keeping the root
# node, all nodes thus visited should be added to the root node

# Every time you go to an unvisited node, do the following if it is a land:
# - Set its root node to the root node parameter. If the root node parameter
#   is (-1, -1), then this is a new island. Set root node to (x,y)
# - Recursively call DFS with root node = root node for each adjacent unvisited cell

# Upon going to an unvisited node, do the following if it is sea:
# - Set its root node to -1

# At the end of the traversal, each node will have a root node.
# Count the number of unique root nodes to get the number of islands.


class Solution:
    def dfs(self, matrix):

        # Step 0. Check for empty input
        if not matrix:
            return []

        # Step 1. Initialisation
        rows, cols = len(matrix), len(matrix[0])
        visited = {}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2. Define the traversal function
        def traverse(i, j, root_node):
            if (i, j) in visited:
                return
            # If not visited, then we think about what to do
            # visited.add(i,j)
            if matrix[i][j] == '0':  # Sea
                root_node = (-1, -1)

            else:  # This is an island
                if root_node == (-1, -1):  # This is a new island
                    # Set the root node of this node to itself
                    root_node = (i, j)
                else:  # This is not a new island: its root node was a land
                    pass

            visited[(i, j)] = root_node  # Set visited to the root node

            if matrix[i][j] == '1':  # We only keep traversing if we are on land
                for direction in directions:
                    next_i, next_j = i + direction[0], j + direction[1]
                    # Does it matter if i traverse all nodes or just the land nodes?
                    # Check this with kuan
                    # Set the root node to the root node of this node
                    if 0 <= next_i < rows and 0 <= next_j < cols:
                        traverse(next_i, next_j, root_node)

        # Steo 3, Traverse every point in the matrix.
        for i in range(rows):
            for j in range(cols):
                traverse(i, j, (-1, -1))
        return visited

    def countNumIslands(self, visited) -> int:
        if not visited:
            return 0

        islands = set()
        num_islands = 0
        for key in visited:
            islands.add(visited[key])

        for island in islands:
            if island != (-1, -1):
                num_islands += 1
        print(islands)
        return num_islands

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = self.dfs(grid)
        num_islands = self.countNumIslands(visited)
        return num_islands


def s(grid):
    sol = Solution()
    print(sol.numIslands(grid))


'''

s([])  # 0
s([["1"]])  # 0

s([["1", "1", "1", "1", "0"],
   ["1", "1", "0", "1", "0"],
   ["1", "1", "0", "0", "0"],
   ["0", "0", "0", "0", "0"]])  # 1

s([
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
  ])  # 3

s([
  ["0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "0", "0"]
  ])  # 1

s([
  ["0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0"]
  ])  # 0
'''
