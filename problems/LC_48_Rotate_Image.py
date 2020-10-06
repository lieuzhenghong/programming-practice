'''
48. Rotate Image
Medium

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

Example 3:

Input: matrix = [[1]]
Output: [[1]]

Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]



Constraints:

    matrix.length == n
    matrix[i].length == n
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
'''

# Attempted Thursday 1st October, 2000
# Submitted 2025

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates a matrix in place
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        start = 0

        while size > 1:
            for i in range(size - 1):
                # Do a four-cycle
                a = matrix[start+0][start+i]
                b = matrix[start+i][-(start+1)]
                c = matrix[-(start+1)][-(start+i+1)]
                d = matrix[-(start+1+i)][start+0]
                # print(a, b, c, d)
                matrix[start+i][-(start+1)] = a  # b <- a
                matrix[-(start+1)][-(start+i+1)] = b  # c <- b
                matrix[-(start+1+i)][start+0] = c  # d <- c
                matrix[start+0][start+i] = d  # a <- d

            size -= 2
            start += 1

        print(matrix)


'''
Let's trace!

rotate([]) => nothing happens since size = 0
rotate([1]) => nothing happens since size = 1
rotate([1,2], [3,4]) =>
    size = 2
    start = 0
    for i in range(1):
        a = matrix[0][0] # 1
        b = matrix[0][-1] # 2
        c = matrix[-1][-1] # 4
        d = matrix[-1][0] # 3
        reassignments
    size -= 2 # size = 0
    start += 1
    terminated since size <= 1

'''

'''
1 2 3       7 9 1
4 5 6 ->    4 5 2
7 8 9       3 8 6

1 2     3 1    
3 4     4 2
'''

print(Solution().rotate(matrix=[[1, 2], [3, 4]]))
print(Solution().rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(Solution().rotate(matrix=[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]))
