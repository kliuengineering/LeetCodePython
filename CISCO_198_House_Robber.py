from typing import List


# below is a wrong solution
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         """
#         return max

#         """

#         MAX = len(nums)
#         rob1, rob2 = 0, 0
#         i = 0

#         while i < MAX:
#             if i % 2 == 0:
#                 rob2 += nums[i]
#             else:
#                 rob1 += nums[i]
#             i += 1

#         return max(rob1, rob2)


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        
        suppose nums = [1, 2, 3, 2, 1, 4, 7]
                        |  |  |  |
                                 cu

        base case:  if len(nums) == 0, then return null
                    if len(nums) == 1, then return nums[0]
                    if len(nums) == 2, then return max(a, b)

        induction:  max(current + a, b)
        
        """

        a = 0
        b = 0

        for curr in nums:
            cache = max( curr + a, b )
            a = b
            b = cache

        return b

                   
def main():
    solution = Solution()
    nums1 = [1, 2, 3, 5]
    nums2 = [2, 7, 9, 3, 1]
    nums3 = [2, 1, 1, 2]

    print(solution.rob(nums1))
    print(solution.rob(nums2))
    print(solution.rob(nums3))


if __name__ == "__main__":
    main()