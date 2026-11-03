class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0

        res_l, res_r = -1, -1

        for i in range(n):
            l, r = i, i

            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                if max_len < (r-l+1):
                    max_len = r-l+1
                    res_l = l
                    res_r = r
                l -= 1
                r += 1
            
            l, r = i-1, i

            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                if max_len < (r-l+1):
                    max_len = r-l+1
                    res_l = l
                    res_r = r
                l -= 1
                r += 1
        
        return s[res_l:res_r+1] if max_len else ""