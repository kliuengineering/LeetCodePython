from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        def BinarySearchRow(top: int, bot: int) -> bool:
            # typical binary search
            def BinarySearchCol(row: int, left: int, right: int) -> bool:
                if left > right:
                    return False
                
                midc = (left + right) // 2
                if target == matrix[row][midc]:
                    return True
                elif target > matrix[row][midc]:
                    return BinarySearchCol(row, midc+1, right)
                else:
                    return BinarySearchCol(row, left, midc-1)
                
            # target not in matrix
            if top > bot:
                return False
            
            midr = (top + bot) // 2

            if target == matrix[midr][0]:
                return True
            elif top == bot:
                return BinarySearchCol(top, 0, n-1)
            # can the target be in this row?
            elif matrix[midr][0] < target <= matrix[midr][-1]:
                return BinarySearchCol(midr, 0, n-1)
            elif target > matrix[midr][0]:
                return BinarySearchRow(midr+1, bot)
            else:
                return BinarySearchRow(top, midr-1)
            
        # starts search
        return BinarySearchRow(0, m-1)


def main():
    solution = Solution()
    matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target=3

    print( solution.searchMatrix(matrix, target) )


if __name__ == "__main__":
    main()