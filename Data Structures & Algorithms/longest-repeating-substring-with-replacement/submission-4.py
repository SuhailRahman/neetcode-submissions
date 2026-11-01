class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 1
        n = len(s)

        # for i in range(n):
        #     count, max_f = dict(), 0
        #     for j in range(i, n):
        #         count[s[j]] = 1 + count.get(s[j],0)
        #         max_f = max(count.values())
        #         if (j-i+1) - max_f <= k:
        #             longest = max(longest, j-i+1)
        # return longest

        l, r = 0, 0
        count = dict()
        while r < n:
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(count.values())
            while (r-l+1) - max_f > k:
                count[s[l]] -= 1
                l += 1
                max_f = max(count.values())
            longest = max(longest, r-l+1)
            r += 1
        return longest



