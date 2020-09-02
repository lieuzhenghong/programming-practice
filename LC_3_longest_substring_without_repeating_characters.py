'''

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

# Idea is as follows.
# Keep a left pointer and a right pointer.
# Walk through the string.
# The left pointer points to the earliest nonrepeated letter.
# The right pointer is the current index.
# Keep a data structure like this:
# {a: [], b: [0, 2], c: [1, 5], d: [3] ...}
# basically indexing where the letters appear in the string.
# We initialise left and right pointer at 0.
# Then we start moving the right pointer.
# Look at the character under the right pointer.
# Then check: Is the character repeated?
# Do this check by looking in the dictionary,
# finding the last element of that array value,
# and seeing if that last element <> left pointer.
# If last element > left pointer: we have a repeat.
#   - Write down the length of the substring,
#   - move the left pointer to last element + 1,
#   - and continue.
# If last element < left pointer: we have no repeat. Continue.
# Add the index to the dictionary.
# When the right pointer reaches the end of the string,
# check the current length,
# return the max length.

# Started 1405, ended 1455. Why? Careless, missed out stuff...
# 50 minutes to solve this problem


class Solution:

    def character_is_repeated(self, c: str, left_pointer: int, lookup_table) -> bool:
        # Character is repeated iff
        # the rightmost occurrence of the character i
        # is greater than, or equal to, the left pointer
        return lookup_table[c][-1] >= left_pointer

    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup_table = {}
        left_pointer = 0
        max_length = 0
        current_length = 0
        # We're going to start moving.
        for right_pointer, c in enumerate(s):
            if c not in lookup_table:
                lookup_table[c] = [right_pointer]
                current_length += 1
            else:
                # We check if there's a repeated character
                if self.character_is_repeated(c, left_pointer, lookup_table):
                    # Move left pointer to the position after the repeated character
                    left_pointer = lookup_table[c][-1] + 1
                    # Add latest character to the lookup table
                    max_length = current_length if current_length > max_length else max_length
                    # Set up the new current length
                    current_length = right_pointer - left_pointer + 1
                else:
                    current_length += 1
                lookup_table[c].append(right_pointer)

        max_length = current_length if current_length > max_length else max_length
        return max_length


# pwwkewabcdf
sol = Solution()

# aabaab!bb
print(sol.lengthOfLongestSubstring("aabaab!bb"))  # 3

'''
# pwwkewabcdf
print(sol.lengthOfLongestSubstring("pwwkewabcdf"))  # 8

# abcabcbb
print(sol.lengthOfLongestSubstring("abcabcbb"))  # 3

# bbbbb
print(sol.lengthOfLongestSubstring("bbbbb"))  # 1

# pwwkew
print(sol.lengthOfLongestSubstring("pwwkew"))  # 3

# Empty string
print(sol.lengthOfLongestSubstring(""))  # 0

# One character
print(sol.lengthOfLongestSubstring("b"))  # 1

# tmmzuxt
print(sol.lengthOfLongestSubstring("tmmzuxt"))  # 5
'''
