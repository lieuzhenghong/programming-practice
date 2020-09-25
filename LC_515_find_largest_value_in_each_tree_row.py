'''
515. Find Largest Value in Each Tree Row
 Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

 Definition for a binary tree node.
 class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
'''

# Mike gave me this question in our interview. 24th September 2020.
# Pretty easy and straightforward recursive implementation: solved in 15 minutes

# Note that Python 3.6's dict is now ordered by insertion order
# (reducing the usefulness of OrderedDict).

from collections import OrderedDict


class Solution:
    def traverse(self, node: TreeNode, depth: int, max_val: List[int]):
        if not node:
            pass
        else:
            if depth not in max_val:
                max_val[depth] = node.val
            else:
                max_val[depth] = max(node.val, max_val[depth])
            self.traverse(node.left, depth+1, max_val)
            self.traverse(node.right, depth+1, max_val)

    def largestValues(self, root: TreeNode) -> List[int]:
        max_val = OrderedDict()
        self.traverse(root, 0, max_val)
        return [value for key, value in max_val.items()]


'''
Runtime: 44 ms, faster than 89.93% of Python3 online submissions for Find Largest Value in Each Tree Row.
Memory Usage: 16.4 MB, less than 23.58% of Python3 online submissions for Find Largest Value in Each Tree Row.
'''
