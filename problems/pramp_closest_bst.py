'''
# I was given this question by Mike after I solved that honestly rather trivial 2-SUM problem
# Started around 2352 (7 minutes in after I did the merge_2_packages problem)
# This one was a bit interesting. I was worried that I wouldn't be able to do BST
# because I hadn't practiced much but it was actually OK
# Generally the Pramp problems seem too easy, or is it just me?
# They don't adequately prepare algo skills. But helpful for learning how to talk through problem.

Mike's feedback:

**Things you did well**:

Explained high-level algorithm well. Elegantly described properties of
problem space. Defined class before coding Clean code (after refactor) Very
comprehensive trace.

**Things you should work on**:

You can move very quickly. Make sure the interviewer is keeping up. Try not
to read the code verbatim as you trace. You plain English comments helped
though! '''

'''
== Problem statement == 

Finding the closest value in a BST to a target value
BST is comprised of left, right and val
Property of BST: val > left, val <= right

Example:
         10
       /     \
      5      22
    /   \   /   \
   2     5 13   22
 /           \
1            14

target = 12
returns 13
'''


class bst:
    def __init__(self, left: bst | None, right: bst | None, val):
        self.val = val
        self.left = left
        self.right = right


def find_closest(tree: bst, target):
    closest_number = None
    closest_delta = float("inf")
    # Let's handle the base case
    curr = tree

    while (curr.left is not None or curr.right is not None):  # We can keep going
        delta = abs(target - curr.val)
        if delta < closest_delta:
            closest_delta = delta
            closest_number = curr.val

        if curr.val == target:
            return target
        if target >= curr.val and curr.right is not None:  # We should go right
            curr = curr.right  # Gone right
        elif target < curr.val and curr.left is not None:  # We should go left
            curr = curr.left
        else:  # We've reached a root
            return closest_number

    return closest_number


'''
      =  10
       /     \
      5      22
    /   \   /   \
   2     5 13   22
 /           \
1            14

target = 12
returns 13

== TRACE ==

curr = bst(10). Since 10 != 12, enter while loop
while:
  delta = abs(10-12) = 2
  since 2 < Inf
  closest_delta = 2
  closest_number = 10
  
  12 > 10 and curr right not none:
  curr = bst(22)
  delta = abs(12 - 22)
  12 < 22 and left not none:
  curr = bst(13)
  
  delta = abs(13-12) = 1
  since 1 < 2, closest_delta = 1 closest number = 13
  13 > 12 BUT curr.right IS none, hence we drop to the else
  and we return closest_number = 13
  
'''
