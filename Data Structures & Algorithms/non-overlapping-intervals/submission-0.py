class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        stack = []
        min_removed = 0
        for s, e in intervals:
            if not stack or stack[-1][1] <= s:
                stack.append([s, e])
            else:
                prev_interval = stack.pop()
                if prev_interval[1] > e:
                    stack.append([s, e])
                else:
                    stack.append(prev_interval) 
                min_removed += 1
        
        return min_removed