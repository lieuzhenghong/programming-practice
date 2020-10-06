'''
226. Invert Binary Tree

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9

Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

    Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

Attempted September 16th 2020, 2355
Solved September 17th 2020: 0006: easy recursive function call
Need to write a helper function to generate the binary tree from a list input
Otherwise cannot test

Took five minutes to look at the solution and do something more elegant
'''

# My idea here:
# Just flip the left and right children

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def flipLeftAndRightChildren(self, node: TreeNode) -> TreeNode:
        '''
        Recursive function that flips the left and right children 
        of a binary tree node

        First, handle the base case
        The base case is if I have no children

        The next base case if I have only one child (left or right)

        Otherwise, recursively call flipLeftAndRightChildren on my children
        '''
        if not node:
            pass
        else:
            new_right = self.flipLeftAndRightChildren(node.left)
            node.left = self.flipLeftAndRightChildren(node.right)
            node.right = new_right
        return node

    def invertTree(self, root: TreeNode) -> TreeNode:
        return self.flipLeftAndRightChildren(root)
