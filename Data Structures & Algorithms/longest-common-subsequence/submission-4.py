class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # cache = dict()
        # def lCS(s1, s2, i, j):
        #     if i == len(s1) or j == len(s2):
        #         return 0
        #     if (i, j) in cache:
        #         return cache[(i, j)]
        #     res = lCS(s1, s2, i, j+1)
        #     res = max(res, lCS(s1, s2, i+1, j))
        #     if s1[i] == s2[j]:
        #         res = max(res, 1 + lCS(s1, s2, i+1, j+1))
        #     cache[(i, j)] = res
        #     return cache[(i, j)]
        
        # return lCS(text1, text2, 0, 0)
        m = len(text1)
        n = len(text2)
        s1 = text1
        s2 = text2
        curRow = [0] * (n+1) 

        for i in range(m-1, -1, -1):
            newRow = [0] * (n+1)
            for j in range(n-1, -1, -1):
                newRow[j] = max(curRow[j], newRow[j+1])
                if s1[i] == s2[j]:
                    newRow[j] = max(newRow[j], 1 + curRow[j+1])
            curRow = newRow

        return curRow[0]
