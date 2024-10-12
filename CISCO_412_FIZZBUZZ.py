from typing import List


"""

Given:
n: int

Find:
4 cases of computation

"""


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        rc = []

        for i in range(1, n+1):
            if i%3 == 0 and i%5 == 0:
                rc.append("FizzBuzz")
            elif i%3 == 0:
                rc.append("Fizz")
            elif i%5 == 0:
                rc.append("Buzz")
            else:
                rc.append(str(i))

        return rc


def main():
    solution = Solution()
    num = input("Put a number: ")
    print(solution.fizzBuzz(int(num)))


if __name__ == "__main__":
    main()