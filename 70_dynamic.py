class Solution:
    def climbStairs(self, n: int) -> int:
    #     if n < 1:
    #         return 1
    #     elif n == 1:
    #         return 1
    #     else:
    #         return self.climbStairs(n-1) + self.climbStairs(n-2)

        one, two = 1, 1
        for i in range(n-1):
            curr = one
            one = one + two
            two = curr
        return one


def main():
    solution = Solution()
    print( solution.climbStairs(6) )


if __name__ == "__main__":
    main()