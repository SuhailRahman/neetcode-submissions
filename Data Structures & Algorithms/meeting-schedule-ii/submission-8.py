"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = dict()
        for i in intervals:
            s, e = i.start, i.end
            mp[s] = 1 + mp.get(s, 0)
            mp[e] = mp.get(e, 0) - 1
        res = 0
        rooms = 0
        for key in sorted(mp.keys()):
            rooms += mp[key]
            res = max(res, rooms)
        # print(mp, res, rooms)
        return res