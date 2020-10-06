from typing import Sequence, Callable, TypeVar, Tuple

T = TypeVar('T')


def bisect_right(a, n, f):
    '''
    Copied and modified from the bisect library.
    '''
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi)//2
        if f is None:
            cond = a[mid] > n
        else:
            cond = f(a[mid]) > n
        if cond:
            hi = mid
        else:
            lo = mid+1
    return lo


def bisect_left(a, n, f=None):
    '''
    Copied and modified from bisect library.
    '''
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi)//2
        if f is None:
            cond = a[mid] < n
        else:
            cond = f(a[mid]) < n
        if cond:
            lo = mid+1
        else:
            hi = mid
    return lo


def binary_search(a: Sequence[T],
                  n: Number,
                  f: Callable[[T], Number]
                  ) -> Tuple(T, i):
    '''
    Searches a sequence of elements Sequence[T] and returns the element T
    that, when called with a function f(T), gives the number N.

    Parameters:
        a: a Sequence of elements of type T. The codomain must be sorted,
           in the sense that f[m] <= f[n] for all m < n.
        f: a Function that takes an element T and returns a Number.
        n: a Number. Note that there must exist some element T such that f(T) = N.

    Returns:
        A tuple of(T, i), where i is the position of T in the Sequence.
    '''
    pass

    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if f(a[mid]) < n:
            lo = mid + 1
        elif f(a[mid]) > n:
            hi = mid
        else:  # We found it!
            return (a[mid], mid)

    return ValueError
