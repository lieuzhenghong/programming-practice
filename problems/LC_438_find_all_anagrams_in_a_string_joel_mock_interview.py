# I was given this as a mock interview question by Joel on the 20th of September 2020

'''
438. Find All Anagrams in a String
Medium

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

'''

from typing import List
from collections import Counter

# Started Sunday Sep 20 2020, 2200.
# Question given 2210
# Solved first naive solution 2220, TLE (we misread the bounds, question was confusing)
# Solved second optimised solution 2256

#


# This solution is correct but TLEd because of bounds
'''
class Solution:
    def isAnagram(self, s: str, p: str, idx: int) -> bool:
        # Returns true iff s[idx:] is an anagram of p
        if not p:
            return False
        substring = s[idx:idx + len(p)]
        return sorted(substring) == sorted(p)

    def findAnagrams(self, s: str, p: str) -> List[int]:
        indices = []
        for i, _ in enumerate(s):
            if self.isAnagram(s, p, i):
                indices.append(i)
        return indices
'''


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:

        if not p:
            return []

        indices = []
        substring = s[0:len(p)]

        s_counter = Counter(substring)
        p_counter = Counter(p)
        delta_counter = Counter()

        for key in s_counter:
            if key in p_counter:
                delta_counter[key] = s_counter[key] - p_counter[key]
            else:
                delta_counter[key] = s_counter[key]
        for key in p_counter:
            if key not in s_counter:
                delta_counter[key] = -p_counter[key]

        for i, char in enumerate(s):
            if i == 0:
                if all([delta_counter[k] == 0 for k in delta_counter]):
                    indices.append(i)
                continue
            # We've dropped the i-1th character
            # And we've added the i+len(p)-1 th character

            if s[i-1] in delta_counter:
                delta_counter[s[i-1]] -= 1
            else:
                delta_counter[s[i-1]] = -1

            if i + len(p)-1 >= len(s):  # We've reached the end of the string
                return indices
            else:
                new_char = s[i+len(p)-1]

                if new_char in delta_counter:
                    delta_counter[new_char] += 1
                else:
                    delta_counter[new_char] = 1

            if all([delta_counter[k] == 0 for k in delta_counter]):
                indices.append(i)

        return indices


def sol(s, p):
    solution = Solution()
    print(solution.findAnagrams(s, p))


sol(s="cbaebabacd", p="abc")  # [0, 6]
sol(s="abab", p="ab")  # [0,1,2]
sol('', '')  # []
sol('A', '')  # []
sol('AAA', 'A')  # [0, 1, 2]
sol('bpaa', 'aa')  # [2]
