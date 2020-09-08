'''
424. Longest Repeating Character Replacement
Medium

Given a string s that consists of only uppercase English letters, you can
perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to
any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters
you can get after performing the above operations.

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
'''

# Let's simplify the problem
# Suppose the problem was
# "Find the length of the longest substring containing all repeating As
# you can get after performing the above operations" --- how would you do it?

# Then repeat it with all 26 letters

# The problem looks quite similar to how to make a contiguous array
# AA0000A0A0A0AAA000A0A --> how do you get the largest contiguous array?
# It's finding the largest contiguous array with k holes, effectively
# Sliding window solution


class Solution():
    def maximumContiguousSubstring(self, s, k, c):
        # print(c)
        l = 0
        num_holes = 0
        max_length = 0

        # Invariant: s[l:r+1] has <= k holes
        for (r, char) in enumerate(s):
            # print(l, r)
            if s[r] != c:
                # We've hit a hole
                num_holes += 1
                while (num_holes > k) and l <= r:
                    # Move the left pointer to the right until string is valid.
                    if s[l] != c:
                        num_holes -= 1
                    l += 1
            max_length = max(r-l+1, max_length)
        return max_length

    def characterReplacement(self, s: str, k: int) -> int:
        # print(s, k)
        max_lengths = {}
        for char in string.ascii_uppercase:
            max_lengths[char] = self.maximumContiguousSubstring(s, k, char)

        # print(f"A: {max_lengths['A']}, B: {max_lengths['B']}")

        return max(max_lengths.values())


def go(s, k):
    sol = Solution()
    print(sol.characterReplacement(s, k))


go(s="ABAB", k=2)
go(s="AABABBA", k=1)
