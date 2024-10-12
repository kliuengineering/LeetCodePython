from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:

        """
        
        Suppose:
        matrix = 1 2 3 4
                 5 6 7 8
                 

        Find:
        num -> min(row) && max(col)

        """

        KB_min = []
        rc = []
        col = len(matrix[0])
        row = len(matrix)

        # find the minimum of each row
        for i in range(row):
            global x, y
            x, y = 0, 0
            global min
            min = float("inf")
            for j in range(col):
                if matrix[i][j] < min:
                    min = matrix[i][j]
                    x, y = i, j
            KB_min.append( (x, y) )
            
        # find the max of KB_row in relation to the matrix
        for itr in KB_min:
            global maxi
            maxi = float("-inf")
            global is_max
            is_max = True
            for i in range(0, row):
                if matrix[i][itr[1]] > matrix[itr[0]][itr[1]]:
                    is_max = False
                    break
            if is_max:
                rc.append( matrix[itr[0]][itr[1]] )

        return rc


def main():
    solution = Solution()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    print(solution.luckyNumbers(matrix))


if __name__ == "__main__":
    main()