class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        if len(intervals) == 0:
            return [newInterval]
        is_inserted = False
        for idx, val in enumerate(intervals):
            s, e = val
            if s > newInterval[0]:
                intervals.insert(idx, newInterval)
                is_inserted = True
                break
        if not is_inserted:
            intervals.append(newInterval)
        for s, e in intervals:
            if not stack or stack[-1][1] < s:
                stack.append([s, e])
            else:
                prev_s, prev_e = stack.pop()
                new_e = max(prev_e, e)
                stack.append([prev_s, new_e])
        # print(stack)
        return stack