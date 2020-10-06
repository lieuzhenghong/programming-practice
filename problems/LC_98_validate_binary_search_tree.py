'''
98. Validate Binary Search Tree
Medium

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.



Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Accepted
766,543
Submissions
2,741,615
'''

# Attempted 28th September 2020, 1930
# Got and traced a solution 2035

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        queue = deque([(root, (float('-inf'), float('inf')))])
        while queue:
            tup = queue.popleft()
            node = tup[0]
            within = tup[1]

            if node.left:
                new_range = (within[0], min(within[1], node.val - 1))
                if node.left.val < new_range[0] or node.left.val > new_range[1]:
                    return False
                else:
                    queue.append((node.left, new_range))
            if node.right:
                new_range = (max(within[0], node.val + 1), within[1])
                if node.right.val < new_range[0] or node.right.val > new_range[1]:
                    return False
                else:
                    queue.append((node.right, new_range))
        return True


# [] # True
# [0] # True
# [2, 1, null] # True
# [2, 1, 3] # True
# [2, 4, 4] # False

'''

Let's trace [2,1,3]

[2,1,3]
queue = [(2, (-inf, inf))]
while queue:
    node = 2
    left = 1

    left:
        new_range = (-inf, 1)
        pass conditions
        queue = [(1, (-inf, 1))]
    right:
        new_range = (3, inf)
        pass conditions
        queue = [(1, (-inf, 1)), (3, (3, inf))]
    
    
    then it just pops the rest of the 2 without any incident
    returns True
        

Let's trace [2,4,4]

[2,4,4]
queue = [(2, (-inf, inf))]
while queue:
    tup = (2, (-inf, inf))
    node = 2
    within = (-inf, inf)
    left = 4
    right = 4

    left:
        new_range = (-inf, min(inf, 2-1))
        new_range = (-inf, 1)
        left.val > 1
            return False

Let's trace:
    5
   / \
  1   9
     / \
    4   6

queue = [(5, (-inf, inf))]
while queue:
    ...
    queue = [(1, (-inf, 4)), (9, (6, inf))]
    ...
    queue = [(9, (6, inf))]
    now looking at left node:
        new_range = (6, 8)
        4 < new_range[0]
        return False
'''

'''
Runtime: 36 ms, faster than 98.22% of Python3 online submissions for Validate Binary Search Tree.
Memory Usage: 16.2 MB, less than 40.32% of Python3 online submissions for Validate Binary Search Tree.
'''
