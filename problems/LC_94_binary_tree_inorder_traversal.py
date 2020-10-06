'''
94. Binary Tree Inorder Traversal
Medium

Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''

# Attempted Friday 2nd October 2020
# Attempted 2135
# Recursive solution 2141
# Attempting iterative solution
# Looked at the answer to implement iterative solution, 2214

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive solution


class Solution:
    def _traverse(self, node: TreeNode) -> List[int]:
        l = []
        if node:
            l += self._traverse(node.left)
            l.append(node.val)
            l += self._traverse(node.right)
        return l

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l = self._traverse(root)
        return l

# Iterative solution


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l, stack = [], [(root, False)]
        curr = root

        while stack:
            curr, visited = stack.pop()
            if not curr:
                continue
            if visited:
                l.append(curr.val)
            else:
                stack.append((curr.right, False))
                stack.append((curr, True))
                stack.append((curr.left, False))
        return l
