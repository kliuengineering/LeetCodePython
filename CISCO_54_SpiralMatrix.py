from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Given:
            matrix[m rows][n columns]
            m != n

        Restrictions:
            m >= 1 rows
            n <= 10 columns

        Square matrix:
            middle element is (m/2, n/2) -> base case and stop

        """


        right = len(matrix[0])
        bot = len(matrix)
        left = 0
        top = 0
        KB = []
        direction = 1           # 1 -> right, 2 -> down, 3 -> left, 4-> up

        while left < right and top < bot:

            if direction == 1:
                for i in range(left, right):
                    KB.append( matrix[top][i] )
                    print("move right")
                top += 1
                direction = 2

            if direction == 2:
                for i in range(top, bot):
                    KB.append( matrix[i][right-1] )
                    print("move down")
                right -= 1
                direction = 3

            if direction == 3:
                if top < bot:
                    for i in range(right-1, left-1, -1):
                        KB.append( matrix[bot-1][i] )
                        print("move left")
                    bot -= 1
                direction = 4

            if direction == 4:
                if left < right:
                    for i in range(bot-1, top-1, -1):
                        KB.append( matrix[i][left] )
                        print("move up")
                    left += 1
                direction = 1

        return KB
    

def main():
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    matrix2 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    solution = Solution()
    print(matrix)
    print("")
    print(solution.spiralOrder(matrix))
    print("")
    print(matrix2)
    print(solution.spiralOrder(matrix2))
    print("")
    
    for i in range(0, 1):
        print(i)
            

if __name__ == "__main__":
    main()