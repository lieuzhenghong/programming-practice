'''
# Started 1h07m
# Solution at 0h25min
# Started writing explanation down

# The key idea of this solution is that a greedy solution will work.
# (Otherwise---as I wasted lots of time on---you'll need a dynamic programming solution.)
# I will now attempt to prove this semi-formally.

# Claim: *any* sequence of valid and mandated removal operations always results in the same final result string

# (Not really a) Proof: 

# The nice thing about this grammar is that the rules ensure no overlaps and no double count.
# For instance, 
# ***BAB*** -> no matter how you remove, result is a B
# The key is that because there's no overlap between the removal rules,
# the __order__ of the removal doesn't matter
# If you had a set of rules that allowed **BA** -> **__**and **AC** -> **__**,
# then it would matter because if you had a string like **BAC** you would be left with a B or a C depending on choice.

# Similarly, if there was a set of rules that allowed 
# [**BAAB** --> **____**, "**AA** --> **__**],
# then it would also matter the order because if you removed the AA prematurely
# you'd be stuck with BB, but if you removed BAAB you'd be able to get rid of the Bs.

# I am certain there is a proof by induction or contradiction or something,
# but I don't have the time to work it out here. (Sorry).

# Corollary: there is only ONE string that satisfies the two conditions
# 1. can be obtained from S by repeatedly applying the described transformation, and
# 2. cannot be further transformed.

# Now that we have the proof, we know that the greedy one-pass solution will work.
# It remains to implement it.
# There are two ways to do it: 
#   1. sliding window with L/R pointer
#   2. a stack.

# A stack is easier and less finicky, so let's go with that.
# The idea is as follows:
# 1. Go through the string and push to the stack
# 2. If you have a valid pair (one of AB, BA, CD, DC) on the top of the stack, pop the pair.
# 3. Repeat this process until the end of the string. At the end, return the stack.

# Again --- this greedy algo ONLY works because 
# any sequence of valid and mandated removal operations results in the same string!

# Algorithmic complexity: 
#  - O(n) time, 
#  - O(n) space 
#   (in the worst case, the entire string can't be popped off and all of that is stored in memory)
'''


def solution(S):
    stack = []
    for char in S:
        if not stack:  # base case
            stack.append(char)
        else:  # Stack isn't empty
            # I sort to avoid doing four different comparisons
            pair = sorted((char, stack[-1]))
            if pair == ['A', 'B'] or pair == ['C', 'D']:
                # pop off last element
                del stack[-1]
            else:  # push new char
                stack.append(char)
    return ''.join(stack)


# Keeping notes here but these are irrelevant -- overcomplicated the question

# So there are couple of transforms we can do
# remove AB
# remove BA
# remove CD
# remove DC

# Does it necessarily have to remove from the end??
# No it doesnt
# Given each string, have to look at all possible removals
# O(n^2) solution? too slow
# For string S:
# - Look at all possible removals by doing sliding window across the entire length of the string
# - Remove them all to get an array of new strings a[]
# - For each new string in a[], recursively call the function
# - this is exponential...
# some sort of dynamic programming?

# CBACD -> CCD -> C
# CBACD -> CBA -> C

# Ah.
# The key is that ...
# have to prove correctness of greedy...
# Claim: *any* sequence of valid removal operations results
# always in the same result string
# Prove by contradiction...
# Intuition is that we must
# Suppose there was

# Prove by induction?
#
