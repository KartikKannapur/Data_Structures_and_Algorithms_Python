"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

"""


class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Method 1:

        * Sum of a continuous range of numbers = n*(n+1)/2
        * Subtract sum(nums) from the number above to find
        the missing number

        Your runtime beats 76.27 % of python submissions.
        """
        n = len(nums)
        return (n * (n + 1) / 2) - sum(nums)