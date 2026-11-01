"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if (intervals[j].start >= intervals[i].start and intervals[j].start < intervals[i].end) or (intervals[j].end > intervals[i].start and intervals[j].end <= intervals[i].end):
                    return False
        return True