from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        last_last, last = 0, 0

        for now in nums:
            temp = max( now + last_last, last )
            last_last = last
            last = temp
        return last
    
def main():
    array = [2, 7, 9, 3, 1]
    solution = Solution()
    print( solution.rob(array) )

if __name__ == "__main__":
    main()