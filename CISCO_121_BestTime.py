from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Given: 
            array
            array[i] == data at index i

        Required:
            max(day1, day2) where day1 == buy, day2 == sell
            return max profit

        Assume:
            prices -> 4, 5, 3, 2, 6, 2 
                      |  |  |  |  |  |
                                  b
                               a
        
        """
        if len(prices) == 0:
            return 0
        
        a = 0
        b = 1
        KB = 0
        
        while( b < len(prices) ):
            if prices[b] < prices[a]:
                a = b
            else:
                KB = max( KB, prices[b] - prices[a] )

            b += 1

        return KB


def main():
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))
    print(prices)


if __name__ == "__main__":
    main()