'''
299. Bulls and Cows
Easy

You are playing the following Bulls and Cows game with your friend: You write
down a number and ask your friend to guess what the number is. Each time your
friend makes a guess, you provide a hint that indicates how many digits in
said guess match your secret number exactly in both digit and position
(called "bulls") and how many digits match the secret number but locate in
the wrong position (called "cows"). Your friend will use successive guesses
and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's
guess, use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.

Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.

Note: You may assume that the secret number and your friend's guess only
contain digits, and their lengths are always equal. '''

# One pass solution.
# The idea is to keep two counters, one for secret and one for guess.
# Then find the intersection of both counters.
# We take the minimum because you can only match at most n tokens

# Solved in 15 minutes during an interviewing.io mock interview
# 11th September 2020 1800--1820


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        assert(len(secret) == len(guess))
        counter_guess = {}
        counter_secret = {}
        num_as = 0
        num_bs = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                num_as += 1
                continue
            else:
                if guess[i] in counter_guess:
                    counter_guess[guess[i]] += 1
                else:
                    counter_guess[guess[i]] = 1
                if secret[i] in counter_secret:
                    counter_secret[secret[i]] += 1
                else:
                    counter_secret[secret[i]] = 1
        for key in counter_guess:
            if key in counter_secret:
                num_bs += min(counter_guess[key], counter_secret[key])
        return f"{num_as}A{num_bs}B"


def s(secret, guess):
    sol = Solution()
    print(sol.getHint(secret, guess))


'''
s(secret="1807", guess="7810")  # 1A3B
s(secret="1123", guess="0111")  # 1A1B
s(secret="1123", guess="0000")  # 0A0B
'''
