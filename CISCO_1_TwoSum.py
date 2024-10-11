from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        
        Given:
            target <- int
            nums <- 2 7 11 15
                    | |
                    a b

        Requirements:
            return a, b -> target == a+b

        Approach:
            in nums? target - curr
        
        """

        KB = {}
        result = []

        for index in range(len(nums)):
            frontier = target - nums[index]

            if frontier not in KB:
                KB[ nums[index] ] = index
            else:
                result.append( KB[frontier] )
                result.append( index )
                break

        return result


def main():
    nums = [2,7,11,15]
    solution = Solution()
    print(solution.twoSum(nums, 22))


if __name__ == "__main__":
    main()