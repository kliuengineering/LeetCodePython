class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j, k = m-1, n-1, m+n-1

        # keeps shifting from the end to start
        while j >= 0 and i >= 0:

            if nums2[j] >= nums1[i]:
                nums1[k] = nums2.pop()
                j -= 1
                k -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1

        # corner case, when array 2 still has elements but array 1 is exhuasted
        while j >= 0:
            nums1[k] = nums2[j]
            k, j = k-1, j-1