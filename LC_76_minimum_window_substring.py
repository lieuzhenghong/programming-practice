'''
76. Minimum Window Substring
Hard

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
    - If there is no such window in S that covers all characters in T, return the empty string "".
    - If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

Started solving 4th September 2020, 1645

09/04/2020 17:36	Accepted	324 ms	15.1 MB	python3
09/04/2020 17:23	Time Limit Exceeded	N/A	N/A	python3
09/04/2020 17:19	Wrong Answer	N/A	N/A	python3
09/04/2020 17:07	Wrong Answer	N/A	N/A	python3
09/04/2020 16:52	Wrong Answer

3 wrong answers, 1 TLE (297/298), 1 accepted.

Took about 70 minutes.

'''

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # The idea is as follows.
        # We keep two pointers and walk through the string.
        # The left and right pointer initialise at 0.
        # Move the right pointer right one at each step.
        # When we see a letter that is in T, we push it to a deque.
        #   - Then, we check if we can move the left pointer to the right.
        #   - We can move the left pointer to the right if there is an "extra letter":
        #   - more formally, if we wanted to move the left pointer
        #   - from point i to a point j, we must make sure that the window from [j,r]
        #   - is still a valid window.
        #   - We do this by using a counter.
        letter_counter = collections.Counter()
        # Initialise the counter and populate it.
        # We initialise it to minus to represent a "deficit" of characters.
        for char in t:
            letter_counter[char] -= 1

        letter_queue = collections.deque()

        l = 0  # Left pointer
        shortest_substring = ''
        for (r, r_char) in enumerate(s):
            if r_char in t:  # If we find a letter that could be in the string, we push it to the queue
                letter_queue.append((r, r_char))
                letter_counter[r_char] += 1
                # Now let's check if we can move the left pointer.
                top_letter: tuple = letter_queue[0]
                while letter_counter[top_letter[1]] > 0:
                    # We can move the left pointer and pop it off the stack
                    # we don't need to keep the top letter because we have an
                    # excess of this letter.
                    # While we have an excess of any letter, just keep popping
                    # off until we can't pop anymore
                    letter_counter[top_letter[1]] -= 1
                    letter_queue.popleft()
                    top_letter = letter_queue[0]
                    l = top_letter[0]
                if letter_counter[top_letter[1]] == 0:
                    # We can't pop this off the stack because we would have
                    # a deficit, but we can safely set l to the top letter's
                    # position (you wouldn't need anything to the left of this)
                    l = top_letter[0]
                    pass
                else:
                    pass

                # Now that we've popped off the top letter and possibly moved
                # the left pointer, let's update the shortest substring.
                # The current substring is valid if and only if
                # we have a excess of letters: that is, if
                # all values in letter_counter are >= 0.
                if all(value >= 0 for value in letter_counter.values()):
                    substring = s[l:r+1]
                    print(shortest_substring)
                    if shortest_substring == '':
                        shortest_substring = substring
                    else:
                        shortest_substring = substring if len(
                            substring) < len(shortest_substring) else shortest_substring

        return shortest_substring
