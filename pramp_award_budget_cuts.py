'''
Award Budget Cuts

The awards committee of your alma mater (i.e. your college/university) asked
for your assistance with a budget allocation problem they’re facing.
Originally, the committee planned to give N research grants this year.
However, due to spending cutbacks, the budget was reduced to newBudget
dollars and now they need to reallocate the grants. The committee made a
decision that they’d like to impact as few grant recipients as possible by
applying a maximum cap on all grants. Every grant initially planned to be
higher than cap will now be exactly cap dollars. Grants less or equal to cap,
obviously, won’t be impacted.

Given an array grantsArray of the original grants and the reduced budget
newBudget, write a function findGrantsCap that finds in the most efficient
manner a cap such that the least number of recipients is impacted and that
the new budget constraint is met (i.e. sum of the N reallocated grants equals
to newBudget).

Analyze the time and space complexities of your solution.

Example:

input: grantsArray = [2, 100, 50, 120, 1000], newBudget = 190

output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190

Constraints:

    [time limit] 5000ms

    [input] array.double grantsArray
        0 ≤ grantsArray.length ≤ 20
        0 ≤ grantsArray[i]

    [input] double newBudget

    [output] double
'''

# Did an interview 21st September 2020, 11--12pm

# Interviewer: this Chinese guy https://www.linkedin.com/in/cloud-huang-a2b516144/
# Started the question at 2330
# Got the binary search algorithm almost immediately, started coding in like 5 minutes
# Had a bit of trouble with the binary search algorithm
# There seem to be many equivalent formulations of the binary search template
# which one is correct??

# I didn't realise that we were supposed to return a float
# Was pretty interesting to do binary search in the non-discreet case
# (you have to have an epsilon but I don't know how that affects time complexity)
# The guy saw that I knew the algorithm and could do it
# and he just did a small tweak and it was all good

# Solved everything in less than 15 minutes with the small tweaks,
# there was a bit of debugging
# The practice with binary search helped, my implementation was actually correct
# even though I was a bit unsteady

# After the interview the guy gave me a different template which I should
# examine and see if I should adopt it or use what I have now


def find_grants_cap(grantsArray, newBudget):
    def sumCap(grantsArray, cap):
        return sum([min(x, cap) for x in grantsArray])

    # We are looking for the largest cap that still falls below newBudget:
    # this is l
    # If we were looking for the smallest cap that still falls ABOVE newBudget
    # then we would be looking for r
    l = 0
    r = max(grantsArray)  # left and right bounds of binary search
    epsilon = 0.001

    while l <= r:
        mid = (float(l) + r) / 2
        budget = sumCap(grantsArray, mid)
        if budget > newBudget:  # We can have a smaller cap
            r = mid - epsilon
        else:
            l = mid + epsilon

    # print(round(l,2))
    return round(l, 2)


find_grants_cap(grantsArray=[2, 100, 50, 120, 1000], newBudget=190)  # 47
find_grants_cap([2, 4], 3)  # 1.5
