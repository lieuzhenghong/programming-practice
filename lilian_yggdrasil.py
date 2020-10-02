'''
# Yggdrasil (80 points)
# CS3230 Design and Analysis of Algorithms
# https://codeforces.com/group/b0nFDNKNrz/contest/293002/problem/A

# Attempted 2nd October 2020, 2330
# Called it a day (partial credit), 0126

## Judgement protocol

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
from sys import stdin


def main():
    # Read input
    r, hmax = map(int, input().split())
    s = stdin.readline()
    a = {}
    isSacred = {}
    numSacred = 0

    for idx, char in enumerate(s):
        if char == 's':
            isSacred[idx+1] = 1

    for idx in range(len(s)-1, -1, -1):
        if idx == len(s)-1:
            a[idx] = int(s[idx-1] == 's')
        else:
            a[idx] = int(s[idx-1] == 's') + a[idx+1]

    memo = {}
    print(solve(0, r, hmax, a, isSacred, memo))
    return memo


def solve(h, r, hmax,  a, isSacred, memo):
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
    # Solve the base cases
    if (h, r) in memo:
        return memo[(h, r)]
    if h > hmax:
        memo[(h, r)] = 0
    elif r == 1:
        # a[h] denotes the number of sacred heights >= h inclusive
        memo[(h, r)] = a[h]
    else:
        memo[(h, r)] = int(h in isSacred) + (max(
            solve(h+r-1, r-1, hmax,  a, isSacred, memo),
            solve(h+r, r, hmax,  a, isSacred, memo),
            solve(h+r+1, r+1, hmax, a, isSacred, memo),
        ))
    return memo[(h, r)]


main()
