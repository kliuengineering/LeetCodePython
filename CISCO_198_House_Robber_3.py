from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        
        suppose we have -> [1, 2, 5, 3, 8, 4]
                            |  |  |  |  |  |
                                           curr   
                                     a  b
        
        cannot have adjacent elements                    
        
        max( curr + a, b )

        """
        
        a = 0
        b = 0
        for curr in nums:
            cache = max(curr + a, b)
            a = b
            b = cache

        return b
            





def main():
    solution = Solution()
    test_list = [1, 2, 5, 3, 8, 4]
    print( solution.rob(test_list) )


if __name__ == "__main__":
    main()