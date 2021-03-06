"""
Given a collection of intervals, find the minimum number of
intervals you need to remove to make the rest of the intervals
non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
Example 1:
Input: [ [1,2], [2,3], [3,4], [1,3] ]

Output: 1

Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:
Input: [ [1,2], [1,2], [1,2] ]

Output: 2

Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:
Input: [ [1,2], [2,3] ]

Output: 0

Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Your runtime beats 73.02 % of python submissions
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        #         # #Method 1
        #         if len(intervals) == 0: return 0
        #         # #Sort the array based on the first element
        #         intervals = (sorted(intervals, key=lambda ele:ele.start))

        #         stack = [intervals[0]]
        #         overlap_counter = 0

        #         for elem in intervals[1:]:
        #             stack_top = stack[-1]

        #             if (stack_top.start <= elem.start) and (elem.end <= stack_top.end):
        #                 overlap_counter += 1
        #             else:
        #                 stack_top.start = min(elem.start, stack_top.start)
        #                 stack_top.end = max(elem.end, stack_top.end)

        #         return(overlap_counter)

        # #Method 2:
        end = float('-inf')
        erased = 0
        for i in sorted(intervals, key=lambda i: i.end):
            if i.start >= end:
                end = i.end
            else:
                erased += 1
        return erased