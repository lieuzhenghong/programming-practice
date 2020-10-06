'''
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself. 
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def traverse_ll(self, l):
        ll = []
        while l:
            ll.append(l.val)
            l = l.next
        print(ll)

    def appendListNode(self, l_from: ListNode,
                       l_to: ListNode, carry: int):
        value = l_from.val + carry
        val = value if value < 10 else value - 10
        carry = 0 if value < 10 else 1
        l_to.next = ListNode(val, next=None)
        return (l_to.next, carry)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        first = None
        last = None
        while l1 and l2:
            value = l1.val + l2.val + carry
            val = value if value < 10 else value - 10
            carry = 0 if value < 10 else 1
            if first is None:  # base case: resultant list is empty
                first = ListNode(val, next=None)
                last = first
            else:
                last.next = ListNode(val, next=None)
                last = last.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            last, carry = self.appendListNode(l1, last, carry)
            l1 = l1.next
        while l2:
            last, carry = self.appendListNode(l2, last, carry)
            l2 = l2.next
        # Last number
        if carry:
            last.next = ListNode(carry, next=None)
            last = last.next

        return first

# Do a couple of edge cases


l1 = ListNode(5)
l2 = ListNode(2)
sol = Solution()
l3 = sol.addTwoNumbers(l1, l2)
sol.traverse_ll(l3)

l1 = ListNode(5)
l2 = ListNode(5)
sol = Solution()
l3 = sol.addTwoNumbers(l1, l2)
sol.traverse_ll(l3)

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
sol = Solution()
l3 = sol.addTwoNumbers(l1, l2)
sol.traverse_ll(l3)


# When one list is longer than the other
l1 = ListNode(3, ListNode(9, ListNode(2, ListNode(1))))
l2 = ListNode(1, ListNode(8))
sol = Solution()
l3 = sol.addTwoNumbers(l1, l2)
sol.traverse_ll(l3)

# When one list is 0
l1 = ListNode(3, ListNode(9, ListNode(2, ListNode(1))))
l2 = ListNode(0)
sol = Solution()
l3 = sol.addTwoNumbers(l1, l2)
sol.traverse_ll(l3)
