'''
79. Word Search
Medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

Constraints:

    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3

Started solve 1600 
Submitted solution 1643, passed after 1 WA.

The DFS recipe really helps: do again to internalise the pattern.

'''

# Idea is as follows.
# For every square run four-direction DFS. For each square,
# initialise a new visited set and run DFS.
# As we traverse, if the final letter is the correct one, return True
# Otherwise, return False

from typing import List


class Solution:
    def dfs(self, board, word) -> bool:
        # Step 0: check edge cases
        if not board:
            return False

        # Step 1: initialise
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: define the traversal function
        def traverse(i, j, word, visited) -> bool:
            # print(f"Traversing {i, j} for {word}, {board[i][j]}")
            if (i, j) in visited:
                # print("Already visited, skipping...")
                return False
            visited.add((i, j))  # Add to visited

            # Now let's traverse. First check if we're done.

            if board[i][j] != word[0]:
                return False
            elif board[i][j] == word[0] and len(word) == 1:
                return True
            else:  # We have a match and we have to keep traversing
                for direction in directions:
                    next_i, next_j = i + direction[0], j + direction[1]
                    if 0 <= next_i < rows and 0 <= next_j < cols:
                        found_word = (
                            traverse(next_i, next_j, word[1:], visited.copy()))
                        if found_word:
                            return True
                return False

        # Step 3: traverse each square
        for i in range(rows):
            for j in range(cols):
                visited = set()
                word_found = traverse(i, j, word, visited)
                if word_found:
                    return True

        # We didn't find the word
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.dfs(board, word)


def s(board, word):
    sol = Solution()
    print(sol.exist(board, word))


'''
s([
], '')  # False


s([
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"]], "ABCCED"
  )  # true

s([
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"]], "SEE"
  )  # true

s([
  ["A", "B", "C", "E"],
  ["S", "F", "C", "S"],
  ["A", "D", "E", "E"]], "ABCD"
  )  # false

s(
    [["a", "b"], ["c", "d"]],
    "cdba"
)  # true
'''
