from typing import List


class Solution:

    def dfs( self, board, row, col, word ):
        # if all letters are found
        if len(word) == 0:                                                                  
            return True
        
        # check valid range
        if  (0 <= row < len(board))     and \
            (0 <= col < len(board[0]))  and \
            board[row][col] != "#"      and \
            board[row][col] == word[0]:                        
            
            cache = board[row][col]
            board[row][col] = "#"

            for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if self.dfs( board, row+i, col+j, word[1:] ):
                    return True
            
            board[row][col] = cache
            return False



    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range( len(board) ):
            for col in range( len(board[0]) ):
                if board[row][col] == word[0]:                                              # try all starting points
                    if self.dfs( board, row, col, word ):
                        return True
        return False


def main():
    matrix = [["1", "2", "3", "4"],
              ["5", "6", "7", "8"],
              ["9", "10", "11", "12"]]
    
    solution = Solution()
    print(solution.exist(matrix, "2376"))


if __name__ == "__main__":
    main()
