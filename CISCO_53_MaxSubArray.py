from typing import List


"""

Input: nums = -2, 1, -3, 4, -1, 2, 1, -5, 4
               |  |  |   



"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        KB = nums[0]
        running_total = 0

        for curr in nums:
            if running_total < 0:
                running_total = 0
            
            running_total += curr

            KB = max( KB, running_total )
        
        return KB


def main():
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()

    print( solution.maxSubArray(array) )


if __name__ == "__main__":
    main()