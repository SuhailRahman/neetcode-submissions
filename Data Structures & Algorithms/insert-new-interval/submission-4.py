class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1

        return res
            
        # stack = []
        # if len(intervals) == 0:
        #     return [newInterval]
        # is_inserted = False
        # for idx, val in enumerate(intervals):
        #     s, e = val
        #     if s > newInterval[0]:
        #         intervals.insert(idx, newInterval)
        #         is_inserted = True
        #         break
        # if not is_inserted:
        #     intervals.append(newInterval)
        # for s, e in intervals:
        #     if not stack or stack[-1][1] < s:
        #         stack.append([s, e])
        #     else:
        #         prev_s, prev_e = stack.pop()
        #         new_e = max(prev_e, e)
        #         stack.append([prev_s, new_e])
        # return stack