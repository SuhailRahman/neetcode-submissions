class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if n < m:
            return ""
        
        resL, resR = -1, -1
        freqS_map, freqT_map = dict(), dict()
        min_length = float("inf")
        need = 0
        for ch in t:
            freqT_map[ch] = 1 + freqT_map.get(ch, 0)
        
        need = len(freqT_map.keys())
        
        have = 0
        l, r = 0, 0
        for r in range(n):
            freqS_map[s[r]] = 1 + freqS_map.get(s[r], 0)

            if s[r] in freqT_map and freqS_map[s[r]] == freqT_map[s[r]]:
                have += 1

            while l <= r and have >= need:
                if min_length > (r-l+1):
                    min_length = r-l+1
                    resR = r
                    resL = l
                freqS_map[s[l]] -= 1
                if s[l] in freqT_map and freqS_map[s[l]] < freqT_map[s[l]]:
                    have -= 1
                l += 1
        
        if resL == -1 and resR == -1:
            return ""
        
        return s[resL:resR+1]
