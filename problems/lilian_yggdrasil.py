'''
# Yggdrasil (80 points)
# CS3230 Design and Analysis of Algorithms
# https://codeforces.com/group/b0nFDNKNrz/contest/293002/problem/A

# Attempted 2nd October 2020, 2330
# Called it a day (partial credit), 0126

# Judgement protocol

Group 1: 8.0 point(s)
Group 2: 7.0 point(s)
Group 3: 10.0 point(s)
Group 4: 21.0 point(s)
Group 5: 0.0 point(s)
Group 6: 0.0 point(s)

=
Points: 46.0
'''
# Passed 1,2,3,4

# from typing import List, Dict
import math
from sys import stdin

# Globals
# memo = {}
r, hmax = map(int, input().split())
s = stdin.readline()

a = [0] * (hmax+1)
isSacred = [False] * (hmax+1)

for idx, char in enumerate(s):
    if char == 's':
        isSacred[idx+1] = True

# Populate the array a
# a[h] denotes the number of sacred heights >= h inclusive
for idx in range(len(s)-1, -1, -1):
    if idx == len(s)-1:
        a[idx] = int(s[idx-1] == 's')
    else:
        a[idx] = (s[idx-1] == 's') + a[idx+1]

memo = [None] * (hmax + 1)
r0 = r
cnt = 1


def solve(h, r, cnt):
    '''
    Returns the number of sacred days.
    Key recurrence relation:
    The maximum number of sacred days at height h and growth rate r =

    (h is a sacred height) + max(
    max number of sacred days at height h+r and growth rate r,
    max number of sacred days at height h+r+1 and growth rate r+1,
    max number of sacred days at height h+r-1 and growth rate r-1
    )
    '''
    # Create the 2D array on demand
    if h > hmax:
        return 0

    if memo[h] is None:
        memo[h] = [None] * (r0 + cnt+1)

    if memo[h][r] is not None:
        return memo[h][r]
    elif r == 1:
        memo[h][r] = a[h]
    else:
        memo[h][r] = int(isSacred[h]) + \
            max(
            solve(h+r, r, cnt+1),
            solve(h+r+1, r+1, cnt+1),
            solve(h+r-1, r-1, cnt+1),
        )
    return memo[h][r]


print(solve(0, r, cnt))

'''
    # Solve the base cases
    if (h, r) in memo:
        return memo[(h, r)]
    if h > hmax:
        memo[(h, r)] = 0
    elif r == 1:
        # a[h] denotes the number of sacred heights >= h inclusive
        memo[(h, r)] = a[h]
    else:
        memo[(h, r)] = int(h in isSacred) + max(
            solve(h+r-1, r-1),
            solve(h+r, r),
            solve(h+r+1, r+1),
        )
    return memo[(h, r)]
    '''


# print(solve(0, r))
