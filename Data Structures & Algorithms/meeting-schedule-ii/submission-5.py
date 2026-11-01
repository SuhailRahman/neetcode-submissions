"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        days = list()
        intervals = sorted(intervals, key = lambda x : x.start)
        for interval in intervals:
            added = False
            for d in days:
                if d.end <= interval.start:
                    d.start = interval.start
                    d.end = interval.end
                    added = True
                    break
            if not added:
                days.append(interval)
        return len(days)
            
            