"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2. The number of elements initialized in nums1 and nums2 are m and n respectively.

Your runtime beats 42.78 % of python submissions.
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        """
        Method 1
        Start iterating from the end of both the arrays.
        At each iteration check if the last element of
        nums1 >= the last element of nums2.
        Append the larger value to the end of the array
        and decrease the indices by 1
        Your runtime beats 42.78 % of python submissions.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1

        # #If nums2 still has elements remaining
        if n > 0:
            nums1[:n] = nums2[:n]

