# Date of interview: 5th September 2020
# Time: 2035
#


# Imagine that you have a grid
# Infinite in three directions (infinite left, up, right)
# Implement a game like Connect 4?


# First step: implement a function that will take a game state
# 1. game state
# 2. the current player
# 3. the current player's move, which is a column number
# return a new game state

from typing import List, Tuple

# A gamestate G is a list of points, where a point is (x, y)
# and x, y are integers. Note that x can be negative, but y >= 0.

# Need some sort of sorted collection that arranges points in lexicographic order

# list of deques, each deque representing a row
# if you want to add to a column that isn't there
# loop through each dequeue and prepend/append an empty space
# and on the bottom dequeue add a piece
# if you add to a column i that is there
# start from the bottom dequeue and check g[0][i] and see if its empty
# do this until you reach for some K, g[k][i] is empty, and fill the space

# or, a Dict of lists, each one representing a column
# have some state saying what the top column number is
# if you want to add to a column that isn't there,
# prepend/append to the Dictionary of lists
# if you want to add a column that is there, simply append to the list
# ok let's go with this

from collections import deque, OrderedDict


def initGameState():
    g = OrderedDict()
    return g


def displayGameBoard(g):
    for k, v in g.items():
        print(f"Column {k}: {v}")

# player 1 is 1, player 2 is 2


def updateGameState(g, c, playernumber: int):
    # g -> h
    # To update a game state, we have to see if that
    # g is a deque of lists
    if c in g:
        g[c].append(playernumber)
    else:  # c not in g:
        g[c] = [playernumber]


def checkIfSomeoneHasWon(g):
    # Returns a player if someone has won
    # Or , -1 otherwise
    # checkHorizontalForWin(g)
    '''
    pass
    checkVerticalForWin(g)
    checkDiagonalForWin(g)
    '''
    pass


def checkRowsForWin(g):
    # This one needs to take the longest column
    # and then check each row using that column's length
    max_length = 0
    winning_player = -1
    for col in g:
        max_length = max(max_length, len(g[col]))
    for i in range(max_length):
        winning_player = checkRowForWin(g, i)
        if (winning_player != -1):
            return winning_player
    return winning_player


def checkRowForWin(g, i):
    '''
    Check the row i for 4 in a row
      |
      v
    1 2 1 
    1 2 2 2 1 2
    2 2
    1
    1
    1 2
    2 1
    1 1
    1 1
    1 1
    '''
    u = 0
    max_length = 0
    current_length = 0
    winning_player = -1
    for col in g:
        if len(g[col]) > i:
            if g[col][i] == g[u][i]:
                current_length += 1
                max_length = max(max_length, current_length)
                if max_length >= 4:
                    return g[col][i]
            else:
                current_length = 1
                max_length = max(max_length, current_length)
                u = col
        else:
            max_length = max(max_length, current_length)
            current_length = 0
            u = col
            continue
    return winning_player


def checkColumnForWin(col: List[int]):
    winning_player = -1
    l = 0
    max_length = 0
    current_length = 0
    for (r, square) in enumerate(col):
        if (col[l] == square):
            current_length += 1
            max_length = max(current_length, max_length)
            if max_length >= 4:
                return square
        else:
            current_length = 1
            l = r
    return winning_player


def checkColumnsForWin(g):
    '''
    Reduce to the problem of checking whether the longest consecutive
    subsequence is 4'''
    winning_player = -1
    for column in g:
        winning_player = checkColumnForWin(g[column])
        if (winning_player != -1):
            return winning_player
    return winning_player


g = initGameState()
# updateGameState(g, 0, 1)
# updateGameState(g, -1, 2)
# updateGameState(g, -2, 1)
# displayGameBoard(g)

print(checkColumnsForWin({0: [1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 2]}))  # 2
print(checkColumnsForWin(
    {0: [1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1],
     1: [2, 2, 2, 1]}))  # -1
print(checkRowsForWin(
    {0: [1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1],
     1: [2, 2, 2, 1],
     2: [2, 2, 2, 1],
     3: [2, 2, 2, 1],
     4: [2, 1, 1, 2],
     }))  # 2
print(checkRowsForWin(
    {0: [1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1],
     1: [2, 2, 2, 1],
     2: [2, 2, 2, 1],
     3: [2, 2, 2, 1],
     4: [1],
     5: [2],
     6: [1, 1, 2, 1],
     6: [2, 1, 1, 2],
     6: [2, 1, 1, 2],
     6: [2, 1, 2, 1],
     }))  # 1

print(checkColumnsForWin(
    {0: [1, 1, 1, 2, 1, 1, 2, 1, 2, 2, 2, 1],
     1: [2, 2, 2, 1],
     2: [2, 2, 2, 1],
     3: [2, 2, 2, 1],
     4: [2, 1, 1, 2],
     }))  # -1
