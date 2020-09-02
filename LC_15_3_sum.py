'''
# LC 15. 3 Sum

Given an array nums of n integers, are there elements a, b, c in nums such
that a + b + c = 0? Find all unique triplets in the array which gives the sum
of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Attempted 2nd September 2020, 1500--1525 (25 minutes)

TLE 278/313 cases, too fat of a solution
Looked at the best solution and I should actually sort the input first
and use three pointers, rather than trying to do what I did
'''

import itertools


class Solution:
    # The idea here is to precompute all possible pairs of a+b.
    # Then iterate through again,
    # and for every element c in nums, find the complement -c = a+b

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        valid_triplets = []
        int_count = {}
        # First let's record how many occurrences of each integer there are
        for num in nums:
            if num not in int_count:
                int_count[num] = 1
            else:
                int_count[num] += 1
        pair_sums = {}
        # Then let's find all the pairwise sums of elements
        for a in nums[:-1]:
            for b in nums[1:]:
                pairsum = a+b
                if pairsum not in pair_sums:
                    pair_sums[pairsum] = [sorted([a, b])]
                else:
                    pair_sums[pairsum].append(sorted([a, b]))
        # Now let's iterate through all the numbers
        # We must first check that there exists some a+b = -c
        # If there is, then we check that neither a or b is actually c
        # And finally we remove duplicates

        for c in nums:
            complement = -c
            if complement not in pair_sums:  # There is no a+b such that a+b+c = 0
                continue
            else:  # We have found pairs
                for a, b in pair_sums[complement]:
                    triplet_int_count = {}
                    if a not in triplet_int_count:
                        triplet_int_count[a] = 1
                    else:
                        triplet_int_count[a] += 1
                    if b not in triplet_int_count:
                        triplet_int_count[b] = 1
                    else:
                        triplet_int_count[b] += 1
                    if c not in triplet_int_count:
                        triplet_int_count[c] = 1
                    else:
                        triplet_int_count[c] += 1
                    # check that all numbers in triplet int count are less
                    # i.e you haven't used the same number twice
                    valid_triplet = True
                    for integer in triplet_int_count:
                        if int_count[integer] < triplet_int_count[integer]:
                            valid_triplet = False
                    # if it is, great: this is a valid triplet
                    if valid_triplet:
                        valid_triplets.append(sorted([a, b, c]))
        valid_triplets = sorted(valid_triplets)
        return list(valid_triplets for valid_triplets, _ in itertools.groupby(valid_triplets))
