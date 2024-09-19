class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        ptr_left, ptr_right = 0, 1
        max_difference = 0

        # single loop, the left ptr "jumps" to the right ptr after meeting a lower right ptr
        while ptr_right < len(prices):
            if prices[ptr_left] < prices[ptr_right]:
                max_difference = max( max_difference, -prices[ptr_left] + prices[ptr_right] )
            else:
                ptr_left = ptr_right
            
            ptr_right += 1

        return max_difference