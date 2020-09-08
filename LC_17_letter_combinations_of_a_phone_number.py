'''
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''

from typing import List
letter_combis = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

# For each character in the string, do a recursive call
# The recursive function should take a digit string,
# as well as a prefix string, and return an arrray of strings


class Solution:
    def recurse(self, prefixes: List[str], digits: str) -> List[str]:
        # Handle the base case first
        if len(digits) == 0:
            return prefixes
        else:
            first_digit = digits[0]
            if first_digit not in letter_combis:
                raise ValueError
            new_prefixes = []
            for i in letter_combis[first_digit]:
                for prefix in prefixes:
                    new_prefixes.append(prefix + i)
            return self.recurse(new_prefixes, digits[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        return self.recurse([''], digits)


def sol(i):
    s = Solution()
    print(s.letterCombinations(i))


sol("23")
sol("22")
sol("27")
