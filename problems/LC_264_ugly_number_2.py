'''
264. Ugly Number II
Medium

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  

    1 is typically treated as an ugly number.
    n does not exceed 1690.

Accepted
185,148
Submissions
438,508
'''

# Main reason for doing this question is to practice heaps and sets
# heapq, sets, etc

# The idea here will be as follows.
# Keep a heap that always has the first n ugly numbers.
# Also keep a temporary Set that holds the ugly numbers of the last iteration.
# At each iteration, multiply all elements in the Set by 2, 3, and 5.
# and make this the Set of the next iteration.
# Push this set into the heap.

import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = []
        heapq.heappush(h, 1)  # initialise the first ugly number
        s = set([1])
        while len(h) < 5 * n:
            # Pretty ugly hack here to make sure we get the nth ugly number
            # I think there is some sort of bound here I just used 5 --- why???
            new_set = set([])
            for i in s:
                new_set.add(i * 2)
                new_set.add(i * 3)
                new_set.add(i * 5)
            # Push all elements in new_set to the heap
            print(new_set)
            for element in new_set:
                heapq.heappush(h, element)
            # Make the new set the set of ugly numbers of the current iteration
            s = new_set

        # Then get the n smallest elements and get the last one for the nth element
        print(heapq.nsmallest(n, h))
        return heapq.nsmallest(n, h)[-1]


def s(n):
    sol = Solution()
    print(sol.nthUglyNumber(n))


s(10)
