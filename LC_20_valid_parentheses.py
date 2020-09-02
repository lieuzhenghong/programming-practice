''' 
## LC 20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '['
and ']', determine if the input string is valid.

An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

Solved 2nd September 2020, 1400--1420 (20 minutes)

== Comments from Wei Heng ==

- Stack class is pointless (problem is already trivial)
- eles doesn't sound good, use elements or elems instead
'''
import typing


class Solution:
    class Stack:

        def __init__(self):
            self.eles = []

        def top(self):
            if not self.eles:
                raise ValueError
            else:
                return self.eles[-1]

        def push(self, ele):
            self.eles.append(ele)

        def pop(self):
            try:
                top_ele = self.top()
            except ValueError:
                raise ValueError
            self.eles = self.eles[:-1]
            return top_ele

    def isValid(self, s: str) -> bool:
        # Idea: use a stack
        # Whenever we see an open bracket, put it on the stack,
        # and whenever we see a close bracket, check if the top item of the stack is the corresponding open bracket
        lookup_table = {
            ')': '(',
            '}': '{',
            ']': '[',
        }
        stack = self.Stack()
        for c in s:
            if c in ['(', '{', '[']:
                stack.push(c)
            elif c in lookup_table:  # one of [')', '}', ']']
                if stack.eles:
                    top_ele = stack.top()
                    if top_ele != lookup_table[c]:
                        return False
                    else:
                        stack.pop()
                else:
                    return False  # stack is prematurely empty
            else:
                raise ValueError

        # At the end, check that the stack is empty
        # If the stack is not empty, there is an unclosed bracket
        if stack.eles:
            return False
        else:
            return True


def test(s):
    sol = Solution()
    print(sol.isValid(s))


test("()")      # True
test("()[]{}")  # True
test("(]")      # False
test("")        # True
test("([)]")    # False
test("{[]}")    # True
