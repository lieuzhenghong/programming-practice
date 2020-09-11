'''
946. Validate Stack Sequences
Medium

Given two sequences pushed and popped with distinct values, return true if
and only if this could have been the result of a sequence of push and pop
operations on an initially empty stack.

Example 1:

Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:

Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

Constraints:

    0 <= pushed.length == popped.length <= 1000
    0 <= pushed[i], popped[i] < 1000
    pushed is a permutation of popped.
    pushed and popped have distinct values.

Solved in 20 minutes for mock interview, 1830--1850
The solution is correct, but non-ideal 
(I should be using dequeue and pointer, and the 
if ele in elements_left check is O(n) time complexity)

I need a quick way to find whether an element is in the list or not
Review this question and do again with Pythonic data structures
'''


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        elements_left = pushed
        for (i, ele) in enumerate(popped):
            # print(i, ele, stack)
            if not stack or stack[-1] != ele:
                if ele in elements_left:
                    while (elements_left[0] != ele):
                        stack.append(elements_left[0])
                        elements_left = elements_left[1:]
                    elements_left = elements_left[1:]
                else:
                    return False
            else:  # stack[-1] == ele:
                stack = stack[:-1]  # pop last element
                continue
        return True
