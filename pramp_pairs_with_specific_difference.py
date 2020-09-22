'''
Pairs with Specific Difference

Given an array arr of distinct integers and a nonnegative integer k, write a function findPairsWithGivenDifference that returns an array of all pairs [x,y] in arr, such that x - y = k. If no such pairs exist, return an empty array.

Note: the order of the pairs in the output array should maintain the order of the y element in the original array.

Examples:

input:  arr = [0, -1, -2, 2, 1], k = 1
output: [[1, 0], [0, -1], [-1, -2], [2, 1]]

input:  arr = [1, 7, 5, 3, 32, 17, 12], k = 17
output: []

Constraints:

    [time limit] 5000ms

    [input] array.integer arr
        0 ≤ arr.length ≤ 100

    [input]integer k
        k ≥ 0

    [output] array.array.integer
'''

# Attempted this question in my first Pramp mock interview
# 21st September 2020, 1745
# Solved relatively in 15 minutes

'''
i just finished interview at pramp
the interview question was too easy for me to practice any communication skill.


=== switch roles ===

My question was basically a variant of 2-sum, I overcomplicated the qn because i didnt see that it was "distinct" integers (so was thinking of doing a for loop from the back so as not to double-count). After this was pointed out to me I solved the question very quickly. Total time taken 15 mins.

Things to take note:

- Be super careful when reading the question and test cases. Actually work through the test cases to see what is wanted. Don't overcomplicate the question.
- Be clear about why I am thinking about what I am thinking about. Like he didn't get me when I was trying the whole backwards traversal thing and had I communicated that more clearly he would have clarified earlier
'''

# x - y = k
# y = x - k




from collections import Counter
def find_pairs_with_given_difference(arr, k):
    c = Counter(arr)  # form a counter
    all_pairs = []
    for y in arr:
        # We are looking for x such that x - k = y
        x = y + k
        if x in c:
            all_pairs.append([x, y])
    return all_pairs

# Helper function


def s(arr, k):
    print(find_pairs_with_given_difference(arr, k))


s(arr=[0, -1, -2, 2, 1], k=1)  # [[1, 0], [0, -1], [-1, -2], [2, 1]]
s(arr=[1, 7, 5, 3, 32, 17, 12], k=17)  # []
