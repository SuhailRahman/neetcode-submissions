class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = dict()
        def lCS(s1, s2, i, j):
            if i == len(s1) or j == len(s2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            res = lCS(s1, s2, i, j+1)
            res = max(res, lCS(s1, s2, i+1, j))
            if s1[i] == s2[j]:
                res = max(res, 1 + lCS(s1, s2, i+1, j+1))
            cache[(i, j)] = res
            return cache[(i, j)]
        
        return lCS(text1, text2, 0, 0)
