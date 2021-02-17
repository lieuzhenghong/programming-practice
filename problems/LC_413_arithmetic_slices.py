class Solution:
    """
    Attempted 2021-02-18
    Took about 25 minutes? Bit rusty. But got it right on the first submission.

    Kind of slow and rusty after taking a break (again). 
    Did this question as part of LeetCode's February Daily Challenge.
    Standard sliding window problem with a bit of a twist.
    I thought about a solution and wrote it down, and it all-cleared on the first try. Very pleased.

    ---

    A sequence of numbers is called arithmetic if it consists of at least three elements and 
    if the difference between any two consecutive elements is the same.

    For example, these are arithmetic sequences:

    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9

    The following sequence is not arithmetic.

    1, 1, 2, 5, 7

    A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

    A slice (P, Q) of the array A is called arithmetic if the sequence:
    A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

    The function should return the number of arithmetic slices in the array A.


    Example:

    A = [1, 2, 3, 4]

    return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
    """
    # Three main invariants:
    # Lemma 1. If A[k, l] is an AS, and A[l-1, l+1] is an AS, A[q, l+1] is an AS for all q >= k <= l-1.
    
    # Lemma 2. if A[k,l] is NOT an AS, then A[k-q, l] is not an AS for all q >= 0.
    
    # Lemma 3. if A[k, l] is NOT an AS, then A[k, l + q] is not an AS for q >= 0 (trivial).
    
    # The following correct algorithm is correct by the Lemmas:
    # Initialise left and right pointer to 0 and 2.
    
    # Sliding window problem.
    # At every step, move the right pointer one step to the right.
    # Check if the last three elements form an AS.
    # If it is not an AS, then it is safe to move the left pointer to the right.
    # This is by Lemma 3 --- all future slices including the left pointer will not be ASes.
    # Move the left pointer and check at each step whether this is an AS,
    # and stop when the size of the slice is 2, or when you have an AS.
    
    # If it is an AS, continue. 
    # Add len(slice) - 2 to the running sum. E.g. if len(slice) is 3, add 1, if len(slice) == 4 add 2.
    
    # Time complexity: O(n). Worst case scenario, left pointer and right pointer both traverse the list.
    # Memory complexity: O(1).
    
    def _is_as_(self, S: List[int]) -> bool:
        assert(len(S) == 3)
        return (S[1] - S[0]) == (S[2] - S[1])
    
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        l = 0
        running_sum = 0
        
        for r in range(2, len(A)):
            if self._is_as_(A[r-2:r+1]):
                running_sum += ((r+1 - l) - 2)
                continue
            else:
                # Move left until you hit an AS or until you hit a slice of 2
                while r > l + 1:
                    l += 1
                    # note that this check is safe, since left pointer always points to
                    # either the start of a slice of 2, or the start of an AS.
                    if (A[l+1] - A[l] == A[r] - A[r-1]):
                        break
                        
        return running_sum
                        
                        
            
        