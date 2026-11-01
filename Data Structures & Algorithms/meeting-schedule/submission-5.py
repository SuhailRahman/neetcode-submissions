"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda x : x.start)
        stack = list()
        for interval in intervals:
            if not stack or stack[-1][1] <= interval.start:
                stack.append([interval.start, interval.end])
            else:
                return False
        return True