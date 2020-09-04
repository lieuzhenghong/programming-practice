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


class Solution:
    def maximumContiguousSubStringWithKHoles(self, s: str, k: int, c: str) -> int:
        '''
        Given a string AA0000A0A0A0AAA000A0A,
        what is the maximum length of the contiguous substring with K holes?
        In this case, if k = 3, and c = "A",
        then the maximum length would be 9 (fill the 0s in the middle)
        '''
        left_ptr = 0
        right_ptr = 0
        holes_left = k
        max_length = 0
        current_length = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        while right_ptr <= len(s):
            if k[left_ptr] != c:

            elif k[right_ptr] != c:
                if holes_left:
                    holes_left -= 1
                    le

            else:
                right_ptr += 1
                current_length += 1
                max_length = max(current_length, max_length)

        pass

    def characterReplacement(self, s: str, k: int) -> int:
        pass
