class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = []

        for s, e in intervals:
            if not stack or stack[-1][1] < s:
                stack.append([s, e])
            else:
                prev_s, prev_e = stack.pop()
                new_s = min(s, prev_s)
                new_e = max(e, prev_e)
                stack.append([new_s, new_e])
        return stack