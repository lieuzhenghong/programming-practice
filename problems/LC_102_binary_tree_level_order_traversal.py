'''
102. Binary Tree Level Order Traversal
Medium

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

Accepted
674,252
Submissions
1,222,130
'''

# Attempted Sunday 27th September 2020, 0140
# Took about 15 minutes.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque([(root, 0)])
        traversal = defaultdict(list)
        while queue:
            elem = queue.popleft()
            node = elem[0]
            depth = elem[1]
            if node:
                left = node.left
                right = node.right
                traversal[depth].append(node.val)
                queue.append((left, depth+1))
                queue.append((right, depth+1))
        return [traversal[depth] for depth in traversal]


'''
Let's trace:
    3
   / \
  9  20
    /  \
   15   7
traversal = {}
queue = [(3, 0)]

while queue:
    node = 3
    depth = 0
    left = 9
    right = 20
    traversal = {0: [3]}
    queue = [(9, 1), (20, 1)]

    node = 9
    depth = 1
    left = None
    right = None
    traversal = {0: [3], 1:[9]}
    queue = [(20, 1), (None, 2), (None, 2)]

    node = 20
    depth = 1
    left = 15
    right = 7
    traversal = {0: [3], 1:[9, 20]}
    queue = [(None, 2), (None, 2), (15, 2), (7, 2)]

    node = None, queue = [(None, 2), (15, 2), (7, 2)]
    node = None, queue = [(15, 2), (7, 2)]
    node = 15, traversal = {0:[3], 1:[9,20], 2:[15]}, queue = [(7, 2), (None, 3), (None, 3)]
    node = 7, traversal = {0:[3], 1:[9,20], 2:[15,7]}, queue = [(None, 3), (None, 3), (None, 3), (None, 3)]

    ... slowly pops everything off
'''
