from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
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


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    solution = Solution()

    print(matrix)
    solution.rotate(matrix)
    print(matrix)


if __name__ == "__main__":
    main()