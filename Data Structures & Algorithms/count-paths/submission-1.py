class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # cache = dict()
        # def path(r, c):
        #     nonlocal cache
        #     if r == (m-1) and c == (n-1):
        #         return 1
        #     if r == m or c == n:
        #         return 0
        #     if (r, c) in cache:
        #         return cache[(r, c)]
        #     cache[(r, c)] = path(r+1, c) + path(r, c+1)
        #     return cache[(r, c)]
        
        # return path(0,0)

        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == (m-1) and j == (n-1):
                    continue
                dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

    
