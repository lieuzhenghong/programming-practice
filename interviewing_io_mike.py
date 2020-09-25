"""
Given an array of cards as array of integers, rearrange the cards into groups so that each group is size W, and consists of W consecutive cards.


Return true if and only if it is possible.


Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
Output: true
Explanation: Hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

"""

# I was given this question by Mike Rapadas, who in turn got it from a
# FAANG interviewer from interviewing.io
# This was a very interesting problem where I had to use a counter and a deque
# UPDATE: this is wrong

# The first insight is as follows:
# If you start from the minimum element,
# and greedily select from the minimum up
# you are guaranteed to get the right answer if one exists.

# Why is this so? Well, because the minimum element must be paired with
# an element larger than it.
# Any non-minimum element could be paired either downards or upwards.
# So we have to start from the minimum.

# The initial idea was to use only a counter and start from the minimum element
#

# I don't think this time complexity is good though.
# In the worst case the time complexity can be O(n) for removal
# because the deque needs to traverse almost the entire queue
# The deque is NOT a heap! I thought it was.
# The deque is not a priority queue either --- just a doubly-linked list.

# After thinking about it some more and with Wei Heng's help
# I rewrote the solution on 24th September

# MAX_VALUE
# min(hand) = 1
# max(hand) = 1000

from collections import deque, Counter


def arrangeCards(a, w):
    c = Counter(a)
    pq = deque(sorted(a))

    if len(pq) < w:  # Catch edge case
        return False

    while len(pq) > 0:  # Keep trying to form groups of W and we can do this as long as pq is not empty
        min_ele = pq[0]  # check if this peeks
        for i in range(w):
            if (min_ele + i) not in c or c[min_ele + i] == 0:
                return False
            else:
                c[min_ele + i] -= 1
                pq.remove(min_ele + i)
        # We've succesfully made a group of W elements

    return True


def arrangeCards(a, w):
    c = Counter(a)
    if len(a) < w:
        return False

    for i in sorted(list(set(a))):
        if c[i] < 0:
            return False
        if c[i] == 0:
            continue
        n = c[i]
        for j in range(w):
            c[i+j] -= n
            if c[i+j] < 0:
                return False
    return True


print(arrangeCards([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))  # True
print(arrangeCards([1, 2, 3, 6, 2, 3, 4, 7, 8], 4))  # False
print(arrangeCards([], 1))  # False
print(arrangeCards([], 0))  # True
print(arrangeCards(a=[1, 2, 3, 2, 5, 4], w=3))  # False
print(arrangeCards(a=[2, 1, 3, 2, 3, 4], w=3))  # True

'''
# TRACE

hand = [1,2,3,2,5,4],
W = 3

c = {1: 1, 2: 2: 3 :1, 4:1, 5:1}
pq = [1,2,2,3,4,5]

len(pq) > 0 so we enter the while loop

for i in range(3):

  i = 0
  min_ele = pq[0] # Guessing that this will give min element => 1
  if (min_ele + 0) not in c: but it is
    skip
  else:
  c[1] -= 1 => c = {1: 0, 2: 2: 3 :1, 4:1, 5:1}
  pq.remove(1) => [2,2,3,4,5]

  i = 1
  # min_ele = pq[0] => 2
  min_ele is still 1. (assume)
  if (min_ele + 1 => 2) not in c, but it is:
    skip
  else:
  c[2] -= 1 -> {1: 0, 2: 1: 3 :1, 4:1, 5:1}
  pq.remove(2) => [2,3,4,5]

  i = 2
  min ele still 1
  if (3) not in c, but it is:
    skip
  else:
    c[3] -= 1 -> {1: 0, 2: 1: 3 :1, 4:1}
    pq.remove(3) => [2,4,5]

  NOW END OF FOR LOOP

len(pq) > 0 so we go in again

min_ele = pq[0] => 2

for loop
  if (min_ele + 0) not in c: but it is:
    c[2] -= 1 => {1: 0, 2: 0: 5 :1, 4:1}
    pq.remove(2) => [4,5]

  i = 1
  if (min_ele + 1 =>3 ) not in c AND IT ISN'T
    return False

'''


'''
[1,1,1,2,2,2,3,3,3]
{1:3, 2:4, 3:6}

'''
