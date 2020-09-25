'''
139. Word Break
Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

Accepted
604,578
Submissions
1,493,446
'''

# Re-attempted on Thursday 24th September, 2155
# Key recurrence relation:
# s can be decomposed into a dictionary word list
# if and only if
# there exists some n where
# s[:n] is a word and s[n:] can be decomposed into a dictionary word list
# for all n
# Solved 2215. The DP was a bit tricky.
# Submitted and it ran much faster than my original solution
# It's cleaner, too.
# This is quite a good pattern. Might be worth practicing it again.

from typing import List
import collections.abc


class Solution:
    def canBeDecomposed(self, s: str, words, memo) -> bool:
        # Returns true if s can be decomposed into a sequence of dictionary words
        if not s:  # if s is an empty string, it can't be decomposed
            return False

        if s in memo:
            return memo[s]

        if s in words:
            return True

        # Base cases checked: now do recursive call.
        bools = []
        for i in range(len(s)):
            substring = s[:i+1]
            if substring in words:
                memo[substring] = True
                bools.append(self.canBeDecomposed(s[i+1:], words, memo))

        memo[s] = any(bools)
        # Key recurrence relation:
        # s can be decomposed if, for some i:
        # s[:i+1] is a word AND s[i+1:] can be decomposed
        return memo[s]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        result = self.canBeDecomposed(s, words, {})
        return result


def s(s: str, wordDict: List[str]):
    sol = Solution()
    print(sol.wordBreak(s, wordDict))


s("ee", [])  # False
s("leetcode", ["leet", "code"])  # True
s("applepenapple", ["apple", "pen"])  # True
s("catsandog", ["cats", "dog", "sand", "and", "cat"])  # False

'''
Let's trace
"leetcode", l=0
  -> "leetcode" not in memo
  -> l < len(s)
  -> for i in range(len(s[0:])) -> i in range(8):
    -> ... nothing yet
    -> all the way until = 3
    -> substring = s[0:4] = "leet", which is in words
        -> now go down to the recursive call
        -> canbeDecomposed(s, l=4, words, memo)
           -> "leetcode", l=4 -> "code"
           -> "code" IS in words
           -> return True

'''
