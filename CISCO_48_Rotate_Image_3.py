from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        """
        
        suppose matrix A = 
                        1, 2, 3
                        4, 5, 6
                        7, 8, 9

        rotate(A) = 
                        7, 4, 1
                        8, 5, 2
                        9, 6, 3
        
        observation made:
        1) axis rotated, but order remains
        2) same rotational pattern applies to all elements
        
        what we can do:
        1) use pointers to fixate the location of rotation being applied
        2) may declare temporary cache to store the data for rotation

        """

        left, right = 0, len(matrix[0]) - 1

        while left < right:
            top, bot = left, right

            for i in range(right - left):
                cache = matrix[top][left + i]
                matrix[top][left + i] = matrix[bot - i][left]
                matrix[bot - i][left] = matrix[bot][right - i]
                matrix[bot][right - i] = matrix[top + i][right]
                matrix[top + i][right] = cache

                """

                a, b, c, d
                e, f, g, h
                i, j, k, l
                m, n, o, p
                
                """

            left += 1
            right -= 1


def main():
    solution = Solution()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    
    solution.rotate(matrix)
    
    print(matrix)


if __name__ == "__main__":
    main()



