class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_freq_list = [0] * 26
        t_freq_list = [0] * 26
        for ch in s:
            index = ord(ch) - ord('a')
            s_freq_list[index] += 1
        for ch in t:
            index = ord(ch) - ord('a')
            t_freq_list[index] += 1
        for idx in range(26):
            if s_freq_list[idx] != t_freq_list[idx]:
                return False
        return True
