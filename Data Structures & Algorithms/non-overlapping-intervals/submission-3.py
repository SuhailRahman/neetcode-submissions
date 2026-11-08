class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        # stack = []
        prev_end = intervals[0][1]
        min_removed = 0
        for i in range(1,len(intervals)):
            s, e = intervals[i]
            if prev_end > s: 
                if prev_end > e:
                    prev_end = e
                min_removed += 1
            else:
                prev_end = e


            # if not stack or stack[-1][1] <= s:
            #     stack.append([s, e])
            # else:
            #     prev_interval = stack.pop()
            #     if prev_interval[1] > e:
            #         stack.append([s, e])
            #     else:
            #         stack.append(prev_interval) 
            #     min_removed += 1
        
        return min_removed