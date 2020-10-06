'''
875. Koko Eating Bananas
Medium

Koko loves to eat bananas. There are N piles of bananas, the i-th pile has
piles[i] bananas. The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K. Each hour, she
chooses some pile of bananas, and eats K bananas from that pile. If the pile
has less than K bananas, she eats all of them instead, and won't eat any more
bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas
before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H
hours.

Example 1:

Input: piles = [3,6,7,11], H = 8
Output: 4

Example 2:

Input: piles = [30,11,23,4,20], H = 5
Output: 30

Example 3:

Input: piles = [30,11,23,4,20], H = 6
Output: 23

Constraints:

    1 <= piles.length <= 10^4
    piles.length <= H <= 10^9
    1 <= piles[i] <= 10^9

Re-attempted September 20th 2020 1534
1630

Took 45 minutes, this binary search was hard. 
I think the best way is to just reimplement binary search from scratch every time
to practice properly.

'''

# Let's break down the problem.
# Firstly, let's write a function that takes in the bananas per hour eating speed K,
# the piles, and returns the number of hours H0 needed to finish eating the piles.

# Once we have this function, then it's a simple matter of finding the minimum
# eating speed K such that H0 < H

from typing import List
import math


class Solution:
    def hoursNeeded(self, piles: List[int], K: int) -> int:
        # The key to this function is to realise that each pile is independent
        # Koko can eat only from one pile at a time
        # Each pile of N bananas takes ceil(N / K) hours to finish eating.
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/K)
        return hours

    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # Here we do a binary search of H.
        # We know that the minimum speed is 1 and the maximum speed K = max H
        # (because H >= 1)
        # It suffices to do a binary search on hoursNeeded and
        # return the minimum value of K such that H0 <= H.
        l = 1
        r = max(piles)
        minK = r
        while r > l:
            mid = (l + r) // 2
            H0 = self.hoursNeeded(piles, mid)
            if H0 > H:  # Too slow, getting caught
                # this is to prevent looping on sublists of two elements, (0 + 1) // 2 = 0  always
                if l == mid:
                    l = mid + 1
                else:
                    l = mid
            else:  # Too fast: possibly could do better
                minK = min(mid, minK)
                r = mid

        return minK


def s(piles, H) -> int:
    sol = Solution()
    print(sol.minEatingSpeed(piles, H))


s(piles=[3, 6, 7, 11], H=8)  # 4
s(piles=[30, 11, 23, 4, 20], H=5)  # 30
s(piles=[30, 11, 23, 4, 20], H=6)  # 23
s(piles=[312884470], H=968709470)  # 1
