"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1,
if version1 < version2 return -1,
otherwise return 0.

You may assume that the version strings are non-empty
and contain only digits and the . character.
The . character does not represent a decimal point and
is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way
to version three", it is the fifth second-level revision
of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37

Your runtime beats 76.42 % of python submissions.
"""

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        """
        Method 1:
        Your runtime beats 76.42 % of python submissions.
        Split the version numbers based on '.'
        Append zero to the end, to make sure both the 
        version numbers are of the same length.
        Compare
        """
        versions1 = [int(v) for v in version1.split(".")]
        versions2 = [int(v) for v in version2.split(".")]
        for i in range(max(len(versions1),len(versions2))):
            v1 = versions1[i] if i < len(versions1) else 0
            v2 = versions2[i] if i < len(versions2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1;
        return 0;