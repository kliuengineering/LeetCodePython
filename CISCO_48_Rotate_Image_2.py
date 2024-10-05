from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        """

        """
        
        suppose matrix A = 
        1, 2, 3
        4, 5, 6
        7, 8, 9

        rotate(right) = 
        7, 4, 1
        8, 5, 2
        9, 6, 3

        suppose matrix B = 
        a, b, c, d
        e, f, g, h
        i, j, k, l
        m, n, o. p

        rotate(right) =
        m, i, e, a
        n, j, f, b
        o, k, g, c
        p, l, h, d

        observation:
        1) square matrix
        2) relative position changes are systematic
            (0, 0) -> (0, 2) // j+2
            (0, 2) -> (2, 2) // i+2
            (2, 2) -> (2, 0) // j-2
            (2, 0) -> (0, 0) // i-2
        3) backward drawing can be used instead of foward pushing
        
        """

        left = 0
        right = len(matrix[0]) - 1


        while left < right:
            for i in range(right - left):
                top = left
                bot = right

                cache = matrix[top][left + i]
                matrix[top][left + i] = matrix[bot - i][left]
                matrix[bot - i][left] = matrix[bot][right - i]
                matrix[bot][right - i] = matrix[top + i][right]
                matrix[top + i][right] = cache

            left += 1
            right -= 1

    
        


