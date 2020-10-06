'''
424. Longest Repeating Character Replacement
Medium

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Attempt #2: 16th September 2020

Attempted at 1530, finished at 1554

Then looked at the solutions and got another one working at 1610

Total 40 minutes
'''

# Invariant: the sliding window s[l:r+1] cannot have more than k holes
import string
import collections


class Solution:
    def characterReplacement(self, s, k):
        count = collections.Counter()
        start = result = 0

        for end in range(len(s)):
            count[s[end]] += 1
            window_length = end - start + 1
            max_count = count.most_common(1)[0][1]
            if window_length - max_count > k:
                count[s[start]] -= 1
                start += 1
                window_length = end - start + 1
            result = max(result, window_length)
        return result

    def characterReplacement(self, s: str, k: int) -> int:
        # Return the largest sliding window for character C
        counts = collections.Counter()
        l = max_length = 0

        for r, char in enumerate(s):
            counts[char] += 1
            window_length = r-l+1
            max_count = counts.most_common(1)[0][1]
            if window_length - max_count > k:
                counts[s[l]] -= 1
                l += 1
                window_length = r-l+1
            max_length = max(max_length, window_length)

        return max_length


def go(s, k):
    sol = Solution()
    print(sol.characterReplacement(s, k))


go(s="ABAB", k=2)
go(s="AABABBA", k=1)
