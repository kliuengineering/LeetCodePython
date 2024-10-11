from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        output = []
        KB = {}

        for i in range(0, len(nums)):
            x, y = nums[i], target - nums[i]        
            if y not in KB:
                KB[ nums[i] ] = i
            else:
                output.append( i )
                output.append( KB[y] )

        output.sort()
        return output
    

def main():
    MyList = [5, 5]
    target = 10
    solution = Solution()
    print(solution.twoSum(MyList, target))


if __name__ == "__main__":
    main()