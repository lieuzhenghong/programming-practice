from collections import Counter
import random

'''
1713 started
1730 solved part 1
1750 solved part 2, concluded because of lack of time.
'''


# [“orange”, “apple”], [1, 1]
'''
{
    0: 'orange',
    1: 'apple'

    .
    .
    n
}

[orange, apple] [1,3]

{
    0: 'orange'
    1: apple
    2: apple
    3: apple
}

{
    (0,3): 'orange'
    (4,4): 'apple'
}

randomInteger(0, n) => return the correspodning item

{
    0.4: 'orange'
    1: 'apple'
}


[(0.4, 'orange'), ('1', 'apple')]
0.5
0.3


randnum = x
for tup in l:
    if x < tup:
        continue

'''

# My post-mortem thoughts start here

'''
This is the question I was given by Chin Ying:

## Sampling a weighted list of items

Select an item with probability proportional to its weight
Implement the “function”:

weighted_select(items, weights)

where items is a list of strings and weights is a list of integers of the same length as items. The procedure shall randomly output an item from items. The probability of each item being selected shall be proportional to its weight.

Example:
> weighted_select([“orange”, “apple”], [1, 1])
“orange”
> weighted_select([“orange”, “apple”], [1, 1])
“apple”
> weighted_select([“orange”, “apple”], [1, 1])
“apple”
> weighted_select([“orange”, “apple”], [1, 1]) // orange selected 50% of the time
“orange”
> weighted_select([“orange”, “apple”], [0, 1]) // “apple” selected 100% of the time
“apple”

## Allow real-valued weights
Can the previous implementation be modified to support positive real-valued weights? 

> weighted_select([“orange”, “apple”], [0.8, 1.2])
// orange 40% of the time, apple 60%

'''

'''
I considered a couple of different solutions.

There is a solution that takes up in O(W) memory where W is the sum of weights
but all queries henceforth run in O(1) time.
There are other solutions that are more space efficient (O(I)) time
where I is the number of unique elements but that wouldn't run in O(1)
time.

I should have explained that I thought this solution was good because
you usually sample something multiple times so it's more important
that the sampling be fast rather than trying to save memory.

Had a bit of difficulty adding a test function because this function is nondeterministic.
This took up some time.
I suggested two solutions. 
One is to sanity check the dictionary to see if it's correct.
The other is to do Monte Carlo sanity checking:
run the function a large number of times and see if the numbers approximate
the weights.
Chin Ying said let's do the latter.
I was able to get the idea right away but was waylaid by a 
(not very consequential) bug.

The extension was to support positive real-valued weights.
I said that it was possible if you gave up correctness.
Chin Ying asked me to explain.
I said because of floating-point precision,
you will never get exactly the correct weights.
Whereas with integer you will always get the correct answer.
He agreed.

We discussed a bit about the time-space tradeoff.
He said let's assume we accept the tradeoff.
I wrote a solution with the worst-case time complexity of O(I)
to generate the data structure and O(I) per query,
but memory complexity of O(I) as well, which is good if I << W.

The idea is as follows. 
Given the input
```weighted_select([“orange”, “apple”], [0.8, 1.2])```

we form the following sorted list:

[(0.8, 'orange'), ('2', 'apple')]

Then we generate a number between 0 and max. Call this N.
We walk through the list until we find a number such that N < tuple[0]
whereupon we return the number.

The asymptotically optimal solution while keeping memory complexity of O(I)
would be to convert the list

[(0, 0.8, 'orange'), ('0.8, 2', 'apple')]

to a BST which gives us log(I) lookup.
I would not have time to implement it, but it would have been good to mention.

I wrote this to Chin Ying:

Dear Chin Ying,
Thanks for your time today. I loved your qn.
I didn't mention in the interview (panicked)
but the runtime could be improved with a BST.

If we had the list

[(0, 0.8, 'orange'), ('0.8, 2', 'apple')]

we can convert this into a BST which gives us log(I) lookup.

Enjoy Happy Hour!
ZH

--- 

On hindsight, these questions were quite open-ended
and not like the questions I practiced for on Leetcode.
It was a bit sad because I feel like I could do better.
Overall, though, I think I came up with an OK solution.
It wasn't asymptotically optimal but the solution was quite clean
and I correctly identified a time-space complexity tradeoff.

'''


def weighted_select(items, weights):
    counter = 0
    d = {}
    for idx, item in enumerate(items):
        weight = weights[idx]
        for i in range(weight):
            d[counter] = item
            counter += 1
    # We've generated the dictionary
    # Now generate a random number
    print(d)
    sample = random.randint(0, counter-1)
    return (d, counter)


def generate_list(items, weights):
    counter = 0
    l = []
    for idx, item in enumerate(items):
        weight = weights[idx]
        counter += weight
        l.append((counter, item))
    return sorted(l), counter


def _weighted_select(l, counter):
    sample = random.uniform(0, counter)
    # Walk through the list
    for tup in l:
        assert(sample < counter)
        if sample < tup[0]:
            return tup[1]
        else:
            continue


def weighted_select(items, weights):
    # Now generate a random number
    l, counter = generate_list(items, weights)
    # sample = random.randint(0, counter-1)
    return _weighted_select(l, counter)


def test(items, weights):
    a = []
    c = Counter()
    # Run like 1000 times
    l, counter = generate_list(items, weights)
    print(l, counter)
    for i in range(1000):
        c[_weighted_select(l, counter)] += 1
    print(c)
    return c


test(['orange', 'apple'], [1, 1])
test(['orange', 'apple'], [0, 1])
test(['orange', 'apple'], [0.8, 1.2])
test(['orange', 'apple', 'banana'], [0.5, .5, 1])
