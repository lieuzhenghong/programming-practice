'''
25. Reverse Nodes in k-Group
Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

    Could you solve the problem in O(1) extra memory space?
    You may not alter the values in the list's nodes, only nodes itself may be changed.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 0947
# Solved 1115 - 90 minutes

'''
1. Initialise two pointers at the head of the LL.
2. Move the right pointer k-1 nodes forward. (It should now be at the kth node).
3. If the right pointer is None, return the left pointer.

 
4. Store the left pointer in memory. Label this first and store it in memory.
5. Start walking both pointers k steps. At every step, reverse the linked list at the left pointer. (e.g. next -> prev, basic stuff)
6. At the end of k-1 steps, the left pointer (call this curr) will be at the kth LL element. Point first to`curr.next`, completing the reversal of the group of k nodes, 
and move the left pointer to curr.next.
7. Check if the right pointer is None: if not none, repeat steps 4,5,and 6.
'''


def printLN(ln):
    if not ln.next:
        return str(ln.val)
    return str(ln.val) + " > " + printLN(ln.next)


def printLL(ln):
    print(printLN(ln))


def constructLL(a):
    head = constructLN(a)
    return head


def constructLN(a):
    if len(a) == 1:
        return ListNode(a[0], None)
    else:
        return ListNode(a[0], constructLN(a[1:]))


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        curr = r = head
        prev = None
        # Move the right pointer k-1 nodes forward
        for i in range(k-1):
            r = curr.next
            curr = curr.next
            if not r:
                return head

        curr = head  # Reset the curr pointer
        # Now right points to the kth node. which is guaranteed not None
        head = r

        while r:  # Invariant: right always points to the kth node in the grp
            first = curr
            nextstart = r.next
            for i in range(k):
                curr.next, curr, prev = prev, curr.next, curr  # Standard reversing
                if r:
                    r = r.next
            # Two cases. r always points to the rightmost element of the next block.
            # If r exists, then we point the first element of this block
            # to the rightmost element of the next block,
            # and then repeat the reversal.
            # But if r is none, then the next block is smaller and won't be reversed.
            # In that case we simply point the first element of this block
            # to the leftmost element of the next block.
            if r:
                first.next = r
            else:
                first.next = nextstart
        return head


printLL(Solution().reverseKGroup(constructLL([1, 2]), 3))
printLL(Solution().reverseKGroup(constructLL([1, 2, 3, 4, 5]), 2))
printLL(Solution().reverseKGroup(constructLL([1, 2, 3, 4, 5]), 3))

'''
Let's trace!

1 > 2 > 3 > 4 > 5 with k = 2
curr = 1
r = 1
for i in range(1):
    r = head.next
r = 2
right = 2
prev = None
head = 2

while right:
    (right = 2, curr = 1)
    first = 1
    for i in range(2):
        tmp = 2
        1.next = None
        prev = 1
        curr = 2
        r:
            r = 3
        tmp = 3
        2.next = 1
        prev = 2
        curr = 3
        r: r = 4
    since r:
        1.next = 4
    right = 4
    (2 > 1 > 4, 3 > 4 > 5)

    (right == 4, curr == 3, prev == 2)
    first = 3
    for i in range(2):
        tmp = 4
        3.next = 2
        prev = 3
        curr = 4
        r == 4:
            r = 5

        tmp = 5
        4.next = 3
        prev = 4
        curr = 5
        r = None

        since not r:
            3.next = 5
        right = None






'''
