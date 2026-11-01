class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        max_len = 1
        l = 0
        visited_map = dict()
        r = 0

        while r < n:
            if s[r] in visited_map and visited_map[s[r]] >= l:
                l = visited_map[s[r]] + 1
            else:
                cur_len = r-l+1
                max_len = max(max_len, cur_len)

            visited_map[s[r]] = r
            r += 1

        cur_len = r - l
        max_len = max(max_len, cur_len)

        return max_len
