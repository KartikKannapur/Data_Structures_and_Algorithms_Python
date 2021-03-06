"""
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input:
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
"""


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        """
        Method 1: Brute Force

        * Iterate through the list of of numbers from lower bound
        to upper bound + 1, to keep it inclusive.
        * For each number, convert the number into a string and 
        check IF there are any zeros in the string
        * Recursively check for divisibility

        Your runtime beats 19.21 % of python3 submissions
        """
        res = []

        for num in range(left, right + 1):
            if str(num).count("0") == 0:
                if all([num % ele == 0 for ele in [int(ele) for ele in set(str(num))]]) == True:
                    res.append(num)
        return res