'''
104. Maximum Depth of Binary Tree
Easy

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.
Accepted
902,430
Submissions
1,357,110
'''

# Attempted Sunday 27th September 0055. Took about 10 minutes.
# Pretty easy

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def traverse(self, node: TreeNode, depth: int, max_depth: List[int]) -> None:
        if node:
            max_depth[0] = max(max_depth[0], depth)
            self.traverse(node.left, depth+1, max_depth)
            self.traverse(node.right, depth+1, max_depth)

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        maxDepthCounter = [1]
        self.traverse(root, 1, maxDepthCounter)
        return maxDepthCounter[0]
