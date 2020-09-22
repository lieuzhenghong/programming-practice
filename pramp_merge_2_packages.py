# I was given this problem in a Pramp peer interview with Mike on 22 Sept 2020
# The problem is trivial --- it's basically 2-SUM
# Mike gave me a hint that I could do it in one pass instead of two
# (which I really should internalise for problems like these)

def get_indices_of_item_weights(arr, limit):
    d = {}

    for i, e in enumerate(arr):
        complement = limit - e
        if complement in d:
            return [i, d[complement][0]]
        if e not in d:
            d[e] = [i]
        else:
            d[e].append(i)

    return []

# == Manual trace ==
# arr = [4, 6, 10, 15, 16],  lim = 21
# i = 0, e = 4 -> complement = 17, complement not in d, e not in d, d[4] = [0]
# i = 1, e = 6 -> comp = 15  .. not in d, e not in d, d[6] = [1]
# i = 2, e = 10 -> comp = 11 ... not in d ... d[10] = [2]
# i = 3, e = 15 -> comp = 6, 6 IS in D, we return (3, 1) and we're done
