"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sortedInterval = sorted(intervals, key = lambda x: x.start)
        for i in range(len(sortedInterval) - 1):
            if sortedInterval[i+1].start < sortedInterval[i].end:
                return False
        return True