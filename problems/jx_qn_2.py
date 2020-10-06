'''
2. Profit Targets
We are looking for distinct pairs
that sum up to exactly target

e.g. stocksProfit = [5,7,9,13,11,6,6,3,3]
target = 12

pairs are (5,7), (3,9), (6,6)

Solved in about 15 minutes?
'''

from collections import defaultdict
from typing import List, Tuple


def profitTarget(stocksProfit: List[int], target: int) -> List[Tuple[int, int]]:
    profitable_pairs = set()
    complements = defaultdict(bool)
    # Complements is a dictionary of
    # int: List[int] denoting the indices of the shares
    for idx, num in enumerate(stocksProfit):
        complement = target - num
        # Look for whether complement in dictionary
        if complement in complements:
            profitable_pairs.add(tuple(sorted((complement, num))))
        complements[num] = True
    return len(profitable_pairs)


assert(profitTarget([], 1) == 0)
assert(profitTarget([1], 0) == 0)
assert(profitTarget([1, -1], 0) == 1)
assert(profitTarget([1, -1], 1) == 0)
assert(profitTarget([1, -1, 1], 0) == 1)
assert(profitTarget([1, -1, 1], 1) == 0)
assert(profitTarget([1, 1, 1], 2) == 1)
assert(profitTarget(stocksProfit=[5, 7, 9, 13, 11, 6, 6, 3, 3],
                    target=12) == 3)
