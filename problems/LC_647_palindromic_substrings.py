'''
647. Palindromic Substrings
Medium

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as
different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".


Note:
    The input string length won't exceed 1000.

Attempted solve 4th September 2020, 1940

Solved at 20:20, 40 minutes afterwards. First dynamic programming solution
in a long time.
# Got a nice AC --- managed to check edge case and debug.
'''

# The key idea to this solution is the following recurrence relation:
# a[i,j] is palindromic iff a[i+1,j-1] is palindromic and a[i] = a[j]
# note if len <= 2 you have to handle the base case
# A simple dynamic programming and memoisation approach should give us an O(n^2) solution


from typing import Dict, Tuple


class Solution:
    def isPalindrome(self, s: str, l: int, r: int, dp) -> bool:
        '''
        Checks if a string is a palindrome
        The key recurrence relation is here:
        a[i,j] is palindromic iff a[i+1,j-1] is palindromic and a[i] = a[j]
        Be sure to memoise
        '''
        if (l, r) in dp:
            return True
        else:
            if (s[l] == s[r] and dp[(l+1, r-1)] is True):
                dp[(l, r)] = True
                return True
            else:
                dp[(l, r)] = False
                return False

    def countSubstrings(self, s: str) -> int:
        # This is a bottom-up dynamic programming solution
        dp = {}
        # First, populate the base case for strings length 1 and 2
        for (i, char) in enumerate(s):
            dp[(i, i)] = True
        # Populate with pairs as well
        for (i, char) in enumerate(s[:-1]):
            dp[(i, i+1)] = (True if s[i] == s[i+1] else False)

        # We've handled the base case; now to do the recursive case
        # We do a recursive call with a sliding window
        # The sliding window works as follows. Initialise a palindrome length
        # and just slide from left to right. Once we hit the right bound,
        # go back to the beginning and increase the palindrome length.
        # "Typewriter" movement
        palindrome_length = 3
        l = 0
        num_palindromes = sum([value for value in dp.values()])
        r = l + palindrome_length
        while r <= len(s):
            # We move the left pointer to the right
            # Doing all palindromes of size palindrome_length
            # Check if s[l:r] is a palindrome
            if self.isPalindrome(s, l, r-1, dp):
                num_palindromes += 1
            l += 1
            r += 1
            if (r > len(s)):
                # Reset everything but increase window size by 1
                palindrome_length += 1
                l = 0
                r = palindrome_length
        # print(dp)
        # print(sum([value for value in dp.values()]))
        return num_palindromes


'''
# A much cleaner and shorter solution I saw on LC after doing the problem

We perform a "center expansion" among all possible centers of the palindrome.

Let N = len(S). There are 2N-1 possible centers for the palindrome: we could
have a center at S[0], between S[0] and S[1], at S[1], between S[1] and S[2],
at S[2], etc.

To iterate over each of the 2N-1 centers, we will move the left pointer every
2 times, and the right pointer every 2 times starting with the second (index
1). Hence, left = center / 2, right = center / 2 + center % 2.

From here, finding every palindrome starting with that center is
straightforward: while the ends are valid and have equal characters, record
the answer and expand.

'''

# The trick here is that the center can be a nothing element.
# I wanted to do the "centers" trick but was stuck because didn't know how to handle
# palindromes of even length


class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        result = 0

        for i in range(2*N-1):
            left = i//2
            right = (i+1)//2
            while left >= 0 and right < N and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1

        return result


def sol(s: str):
    sol = Solution()
    print(sol.countSubstrings(s))


sol("")  # 0
sol("a")  # 1
sol("ab")  # 2
sol("aa")  # 3
sol("abc")  # 3
sol("aaa")  # 6
sol("aaa")  # 6
sol("aaa")  # 6
sol("aaab")  # 7
sol("arbaab")  # 7
