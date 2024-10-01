from typing import List
import random
import sys


class Solution:

    ## inefficient method, O(n^2)
    # def maxSubArray(self, nums: List[int]) -> int:
    #     SIZE = len(nums)
    #     visited = {}

    #     for i in range(0, SIZE):
    #         current_sum = 0
            
    #         for j in range(i, SIZE):
    #             current_sum += nums[j]
    #             visited[current_sum] = (i, j)
            
    #     return max(visited.keys())
            

    # improved -> O(n)
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_array = nums[0]
        current_sum = 0

        for itr in nums:
            if current_sum < 0:
                current_sum = 0

            current_sum += itr
            max_sub_array = max( max_sub_array, current_sum )
        return max_sub_array
    

def MakeArray(nums: List, SIZE) -> List:
    for i in range(0, SIZE):
        nums.append( random.randint(-100, 100) )
    return nums


def main() -> None:
    argv = sys.argv
    if len(argv) > 2:
        raise ValueError("argument needs to be 2")
    
    my_array = []
    my_array = MakeArray( my_array, int(argv[1]) )
    print(my_array)

    solution = Solution()

    print(solution.maxSubArray(my_array))


if __name__ == "__main__":
    main()