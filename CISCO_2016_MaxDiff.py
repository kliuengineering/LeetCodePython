from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        """
        Given:
            nums: array
            n: int

        Find:
            max -> nums[j] - nums[i]

        Rules: 
            1) j > i
            2) nums[j] > nums[i]
        
        Suppose:
            nums = 7, 1, 5, 4
                   |  |  |  |
                   i  j

        Observation:
            if nums[i] >= nums[j] -> then we can move i to j position (rule 2)
            we can use 2 pointers for traversal
            if j reaches the EOL, then we can stop the loop
            i = 0, j = 1 initially

        """

        i = 0
        j = 1
        max_diff = -1
        while j < len(nums):
            if nums[i] >= nums[j]:
                i = j
            else:
                max_diff = max( max_diff, nums[j] - nums[i] )
            j += 1
    
        return max_diff


def main():
    pass


if __name__ == "__main__":
    main()