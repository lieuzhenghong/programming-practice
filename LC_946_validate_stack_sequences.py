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


from typing import List
from collections import deque


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

# Reattempted the solution 1st October 2020, 1700
# Solved AC 1717


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = deque([])
        l = 0
        for ele in popped:
            while len(stack) == 0 or stack[-1] != ele:
                if l == len(pushed):
                    return False
                stack.append(pushed[l])
                l += 1
                if stack[-1] == ele:
                    break
            if stack[-1] == ele:
                stack.pop()
                continue

        return True


'''
Let's trace
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
[]
ele = 4
    while len(pushed) == 0 or stack[-1] != ele:
        len(pushed == 0)
        l != len(pushed)
        stack.append(1)
        stack = [1]
        l = 1

        stack[-1] = 1 != 4
        l != len(pushed)
        stack.append(2)
        stack = [1, 2]
        l = 2

        stack[-1] = 2 != 4
        l != len(pushed)
        stack.append(3)
        stack = [1, 2, 3]
        l = 3

        stack[-1] = 3 != 4
        l != len(pushed)
        stack.append(4)
        stack = [1, 2, 3, 4]
        l = 4
        stack[-1] == 4 == 4
            stack.pop() # stack = [1,2,3]
            continue

ele = 5
    l = 4
    stack[-1] == 4 != 5
    stack.append(pushed[4]) # stack = [1,2,3,5]
    l = 5
    stack[-1] = 5 == ele
    stack.pop() # stack = [1,2,3]

ele = 3
    l = 5
    stack[-1] == 3
'''

assert(Solution().validateStackSequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]) is True)
assert(Solution().validateStackSequences(
    pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]) is False)
