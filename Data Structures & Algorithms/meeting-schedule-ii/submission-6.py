"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res

        # days = list()
        # intervals = sorted(intervals, key = lambda x : x.start)
        # for interval in intervals:
        #     added = False
        #     for d in days:
        #         if d.end <= interval.start:
        #             d.start = interval.start
        #             d.end = interval.end
        #             added = True
        #             break
        #     if not added:
        #         days.append(interval)
        # return len(days)
            
            