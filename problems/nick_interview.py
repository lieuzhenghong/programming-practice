# Question given to me by Nick: apparently it's the actual Digit phone screen q
# Started 1315
# Solved 1330
# [1, 1] infinite loops

from typing import List


def traverse(idx: int, a: List[int], visited: List[int]) -> bool:
    '''Recursive function that returns True iff a zero can be reached
    from the current node index'''
    # When we reach a node, first check if its visited
    # If it is visited, return False, we're done

    # When we reach a node, we check if its 0
    # If it is, return True. We're done

    # If it isn't 0, then we can move forwards or backwards
    # do recursive call on both the forwads and backwards node

    # First check if idx is out of bounds
    if idx < 0 or idx >= len(a):
        return False
    if visited[idx]:
        return False
    if a[idx] == 0:
        return True
    steps = a[idx]  # this won't throw an error because we checked bounds
    visited[idx] = True
    return any([traverse(idx + steps, a, visited),
                traverse(idx - steps, a, visited)]
               )


def findZero(a: List[int]) -> bool:
    visited = [False for _ in a]
    return traverse(0, a, visited)

# [3, 7, 0, 2, 8, 3, 7, 6] # True


def s(a: List[int]):
    r = (findZero(a))
    print(r)
    return r


s([])  # False
s([0])  # True
s([1, 1])  # False
s([1, 0])  # True
s([2, 0])  # False
assert(s([3, 7, 0, 2, 8, 3, 7, 6]) is True)


'''
Trace output
[] => idx = 0 = len([]) => False
[1,0] => idx = 0, a[idx] = 1, visited[1] = True, any(traverse(-1,...), traverse(1...))
    => -1 will return False, and then the a[1] == 0 return True
[1,1]  => idx = 0, a[idx] = 1, visited[1] = True, any(traverse(-1,...), traverse(1...))
        => traverse(0), traverse(2)
        traverse(0) => False because of visited[idx]
        traverse(2) => False because OOB
        => False
[3, 7, 0, 2, 8, 3, 7, 6] # True
    => idx = 0 , a[idx] = 1, any(traverse(-3), traverse(3))
        => traverse(3) => idx = 3, a[idx] = 2, traverse(1), traverse(5)
            => traverse (1) ==> 7 , traverse(-6), traverse(8) => False
            => traverse(5) ==> 3, traverse(2), traverse(8) => False
                => traverse(2) => 0 . So we return True
'''
