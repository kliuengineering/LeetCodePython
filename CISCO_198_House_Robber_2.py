from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        
        [1, 2, 3, 5, 8]
         |  |  |
         a  b  curr

         max( a+curr, b ) // can compute only one of the 2 cases

        """

        a, b = 0, 0
        for curr in nums:
            cache = max( a+curr, b )
            a = b
            b = cache

        return b
    

def power(base, expo) -> int:
    cache = base
    for i in range(0, expo-1):
        base = base*cache
        print(i, " th iteration, base -> ", base)
    return base


def fib(num) -> int:
    if num == 0:
        return 0
    if num == 1:
        return 0
    
    a = 0
    b = 1
    cache = 0
    for i in range(2, num):
        cache = a + b
        a = b
        b = cache
    
    return b


def main():
    array_1 = [1, 2, 3, 5, 8]
    array_2 = [3, 1, 5, 2, 7]
    array_3 = [6, 6, 4, 4]

    solution = Solution()
    print(solution.rob(array_2))

    print( power(2,4) )

    print( "fib num of 7 is ", fib(7) )



if __name__ == "__main__":
    main()