'''
Number of Paths

You’re testing a new driverless car that is located at the Southwest
(bottom-left) corner of an n×n grid. The car is supposed to get to the
opposite, Northeast (top-right), corner of the grid. Given n, the size of the
grid’s axes, write a function numOfPathsToDest that returns the number of the
possible paths the driverless car can take.
alt the car may move only in the white squares

For convenience, let’s represent every square in the grid as a pair (i,j).
The first coordinate in the pair denotes the east-to-west axis, and the
second coordinate denotes the south-to-north axis. The initial state of the
car is (0,0), and the destination is (n-1,n-1).

The car must abide by the following two rules: it cannot cross the diagonal
border. In other words, in every step the position (i,j) needs to maintain i
>= j. See the illustration above for n = 5. In every step, it may go one
square North (up), or one square East (right), but not both. E.g. if the car
is at (3,1), it may go to (3,2) or (4,1).

Explain the correctness of your function, and analyze its time and space
complexities.

Example:

input:  n = 4

output: 5 # since there are five possibilities:
          # “EEENNN”, “EENENN”, “ENEENN”, “ENENEN”, “EENNEN”,
          # where the 'E' character stands for moving one step
          # East, and the 'N' character stands for moving one step
          # North (so, for instance, the path sequence “EEENNN”
          # stands for the following steps that the car took:
          # East, East, East, North, North, North)

Constraints:

    [time limit] 5000ms

    [input] integer n
        1 ≤ n ≤ 100

    [output] integer

'''

# Attempted 21st September 2020 1550
# Solved recursive solution 1600
# Started writing the iterative solution 1603
# Solved the iterative solution 1715

'''
i just finished interview at pramp
the interview question was too easy for me to practice any communication skill.

Got this Indian fella (so far all my mock interviews have been with Indians idk why)

the question that I had to ask was a simple DP problem with the robot moving
up and right counting the number of possible paths. He didn't get it so I fed
him the recurrence relation and walked him through some examples and he
implemented it in the end. I had to help him debug at the end as we were
running out of time.

Total time taken to solve: 45 minutes.

What I learned from interviewing: 

- He was quite clear about what he did and didn't know and I was able to help him
- Not sure when is the right time to jump in as interviewer and give him hint/soln

'''




from typing import Dict, Tuple
def rec(n: int, x: int, y: int, memo: Dict[Tuple[int, int], int]):
    # Handle the base case
    if x == n-1 and y == n-1:
        return 1
    valid_directions = [(1, 0), (0, 1)]
    total_sum = 0
    for direction in valid_directions:
        new_x = x + direction[0]
        new_y = y + direction[1]
        # Check if the new x and new y is a valid square
        if new_x < n and new_y < n and new_x >= new_y:  # Valid dir
            # Check if this square is already memoised
            # If not, do the recursive call
            if (new_x, new_y) not in memo:
                memo[(new_x, new_y)] = rec(n, new_x, new_y, memo)
            total_sum += memo[(new_x, new_y)]
    return total_sum


def num_of_paths_to_dest(n):
    return rec(n, 0, 0, {})


def num_of_paths_to_dest(n):
    # This is an iterative solution
    # A real pain to get right
    print(n)
    up = None  # the number of paths to the destination from the square above
    right = None  # the number of paths to destination from the square to the right
    for j in range(n-1, -1, -1):
        if up is None:
            up = [1]
        for i in range(n-1, j-1, -1):
            print(i, j)
            if right is None:  # First square
                right = [up[-1]]
            else:
                # total ways is equal to the up[] plus the right[]
                # if last square (no up index)
                if i == j:
                    right = [right[0]] + right
                else:
                    # This is the line causing the problem
                    # We need to get the
                    right = [(right[0] + up[i-j-1])] + right
                    # right.append(up[n-1-i] + right[n-1-i])
            total_ways = right[0]  # this is the total ways
        print(up, right)
        up = right
        right = None
    return total_ways


def t(n):
    print(num_of_paths_to_dest(n))


# t(1)  # 1
# t(2)  # 1
# t(3)  # 2
# t(4)  # 5
t(5)  # 14
