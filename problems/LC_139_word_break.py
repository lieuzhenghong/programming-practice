'''
139. Word Break
Medium

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated
sequence of one or more dictionary words.

Note:

- The same word in the dictionary may be reused multiple times in the
segmentation.
- You may assume the dictionary does not contain duplicate words.

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

Attempt 12:34 September
Took a break for lunch than took an hour to do this lol
'''

# Strategy: move the window to the right
# Check if the prefix is in the wordDict
# Recursively call the function to check if the suffix
# is in the wordDict

from typing import List

'''
class Solution:
    def recurse(self, s: str, dp) -> bool:
        if not s:
            dp[s] = True
        elif len(s) == 1:
            a = s in dp and dp[s]
            dp[s] = a
        elif s in dp:
            return dp[s]
        else:
            tentative_bool = False
            for i in range(len(s)-1):
                # Memoise and return the value
                prefix = s[0:i+1]
                suffix = s[i+1:]
                dp[prefix] = self.recurse(prefix, dp)
                dp[suffix] = self.recurse(suffix, dp)
                if dp[prefix] and dp[suffix]:
                    tentative_bool = True
                    dp[s] = True
                    break
            dp[s] = tentative_bool
        return dp[s]

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        for word in wordDict:
            dp[word] = True
        return self.recurse(s, dp)
'''


class Solution:
    # Implemented after looking at the discussions
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        can = [True]
        for i in range(1, len(s)+1):
            can.append(any(can[j] and s[j:i]
                           in wordDict for j in range(i)))
        return can[-1]


def s(s: str, wordDict: List[str]):
    sol = Solution()
    print(sol.wordBreak(s, wordDict))


s("ee", [])  # False
s("leetcode", ["leet", "code"])  # True
s("applepenapple", ["apple", "pen"])  # True
s("catsandog", ["cats", "dog", "sand", "and", "cat"])  # False
