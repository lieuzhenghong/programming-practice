'''

19. Remove Nth Node From End of List
Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

'''

# Get the nth node from the end of the list
# Get the nth-1 node from the end of the list
# Point the nth-1 node to the nth+1 node

# Edge case: if the nth node is at the end or at the start


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # First get the nth node from the end
        # We get the length of the linked list first
        # Then we can get the nth from the end
        ll_length = 1
        curr = head
        while curr.next:
            ll_length += 1
            curr = curr.next

        if n == ll_length:  # They want to remove the first node
            return head.next

        node_id = ll_length - n

        # Now traverse the LL until we get the nth node from the end.

        prev_node = None
        curr_node = head
        next_node = head.next
        i = 0
        while i < node_id:
            prev_node = curr_node
            curr_node = next_node
            if i < ll_length - 1:
                next_node = curr_node.next
            i += 1

        # Now we've reached node_id.
        # Remove it by pointing previous node to next node.
        prev_node.next = next_node
        return head
