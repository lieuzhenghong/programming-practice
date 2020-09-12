''' 
So the input is an array of N integers (items with scores) . You are
supposed to select K integers. But the restriction is, at each choice, you
can only take an integer from either the leftmost or rightmost side of the
array. Once that integer is taken, its gone (they used a supermarket shelf
analogy). Supposed to output maximum score possible.

Attempted let's say 1920, solved 1935
'''

from typing import List


def maxScore(a: List[int], k: int) -> int:
    '''
    Returns the max score
    '''

    memo = {}

    def recurse(a: List[int], l: int, r: int, k: int) -> int:
        '''
        Returns the max score you can get from choosing
        k integers from a subarray of a[l:r+1]

        The key recurrence relation is that
        the maximum sum from the subarray is either
        sum of the LEFT element + the maximum sum in a new subarray 
        without the left element,
        or 
        sum of the RIGHT element + the maximum sum in a new subarray 
        without the right element.
        That is to say, 
        recurse(a, l, r, k) = max(
            recurse(a[l], l+1, r, k-1)
            recurse(a[r], l, r-1, k-1)
        )
        '''
        print(f"Calling {l}, {r}, {k}")
        assert(l <= r)
        # Handle the base case
        if k == 0:
            return 0
        if l == r:
            return a[l]
        elif (l, r) in memo:  # We already have it memoised
            return memo[(l, r)]
        else:
            max_value = max(a[l] + recurse(a, l+1, r, k-1),
                            a[r] + recurse(a, l, r-1, k-1),
                            )
            memo[(l, r)] = max_value
            return max_value

    max_val = recurse(a, 0, len(a)-1, k)
    print(max_val)
    return(max_val)


maxScore([1], 1)  # 1
maxScore([1, 2, 3, 4, 5], 3)  # 12
maxScore([1, 2, 5, 2, 1], 3)  # 8
maxScore([-1, 4, 5, 1, 1], 2)  # 3
maxScore([-1, 4, 5, -1, 1], 4)  # 9
maxScore([1, 1, 1], 3)  # 3
maxScore([], 2)  # AssertionError
maxScore([1, 2, 3, 4, 5], 6)  # AssertionError
