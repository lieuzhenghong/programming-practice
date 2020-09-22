'''
Start 1h40min
Finish 1h25min
# Did this in 15 minutes

# The idea for this solution is as follows.
# The key idea is the following:
# given a number of integers N with identical value V (e.g. in the example there were 3 3's)
# the number of pairs of V are equal to (N)(N-1) / 2.
# This is the identity for the Nth triangular number.
# Consider:
# - 1 element: 0 pairs  (0)
# - 2 element: 1 pair   (1) e.g. 3: (0, 3) --> (0,3) is the only pair
# - 3 elements: 3 pairs (1 + 2) e.g. 3: (0,3,4) --> (0,3), (0,4), (3,4)
# - 4 elements: 6 pairs (1 + 2 + 3) and so on
# - 5 elements: 10 pairs (1 + 2 + 3 + 4)
# And so this can be done in (O(1)).
# And what's left to do is simply to count the number of occurrences that each integer appears.
# This is done with a Counter and takes O(n) space.
# For each element of the Counter we then run through and sum up using the triangle identity described.

# The overall complexity of my solution is:
# - O(n) time,
# - O(100000) -> O(1) space (since N is an integer within the range 0 to 100000)

# ^ Update: this is a mistake, it is actually O(min(N, 2 billion)) -> O(1). 
# Misread the range
'''

from collections import Counter


def solution(A):
    c = Counter(A)
    total_sum = int(sum([(c[n] * (c[n]-1))/2 for n in c]))
    return min(1000000000, total_sum)
