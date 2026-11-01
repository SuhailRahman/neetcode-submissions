class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if n < m:
            return ""
        
        resL, resR = -1, -1
        freqS_map, freqT_map = dict(), dict()
        min_length = float("inf")
        for ch in t:
            freqT_map[ch] = 1 + freqT_map.get(ch, 0)
        
        l, r = 0, 0
        print(freqT_map)
        for r in range(n):
            freqS_map[s[r]] = 1 + freqS_map.get(s[r], 0)
            match = True
            while l <= r and match:
                for ch in freqT_map:
                    if ch not in freqS_map or freqT_map[ch] > freqS_map[ch]:
                        match = False
                        break
                # print(freqS_map, l, r, match)
                if match:
                    if min_length > (r-l+1):
                        min_length = r-l+1
                        resR = r
                        resL = l
                    freqS_map[s[l]] -= 1
                    l += 1
        
        if resL == -1 and resR == -1:
            return ""
        
        return s[resL:resR+1]
