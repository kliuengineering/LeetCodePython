from typing import List


"""

search for 5

1, 2, 3, 5, 7, 9 
|  |  |  |  |  |
l     m        r    -> itr #1
         l  m  r    -> itr #2
         lmr        -> itr #3

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        def recursion(l:int, r:int) -> int:
            rc = -1

            # base case
            if l > r:
                pass

            # gets the mid point
            m = (l + r) // 2

            if target == nums[m]:
                rc = m

            elif target > nums[m]:
                rc = recursion(m, r)

            elif target < nums[m]:
                rc = recursion(l, m-1)

            # returns the search result
            return rc
                
        return recursion(left, right)


def main():
    solution = Solution()
    nums = [-1,0,2,4,6,8] 
    target = 4
    print( solution.search(nums, target) )


if __name__ == "__main__":
    main()