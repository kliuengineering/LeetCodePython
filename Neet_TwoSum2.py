from typing import List

"""

Given:
    numbers: int -> non-decreasing 

Compute:
    a + b == target
    return [a.index, b.index]

restrictions:
          a  < b
    a.index  < b.index
    a.index != b.index

    space -> O(1)

"""


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1
        rc = []

        while a < b:
            sum_curr = numbers[a] + numbers[b]
            if sum_curr == target:
                rc.append(a+1)
                rc.append(b+1)
                break
            elif sum_curr < target:
                a += 1
            else:
                b -= 1

        return rc


def main():
    solution = Solution()
    array = [i for i in range(0, 5)]
    target = 7

    print(solution.twoSum(array, target))


if __name__ == "__main__":
    main()
