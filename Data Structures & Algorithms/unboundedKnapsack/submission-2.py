class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        dp = [[0] * (capacity+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, capacity+1):
                skip = dp[i-1][j]
                include = 0
                if j - weight[i-1] >= 0 :
                    include = profit[i-1] + dp[i][j - weight[i-1]]
                dp[i][j] = max(include, skip)
        return dp[n][capacity]

        # cache = dict()
        # def helper(i, c):
        #     if i == n:
        #         return 0
        #     if (i, c) in cache:
        #         return cache[(i, c)]

        #     skip = helper(i+1, c)
        #     include = 0

        #     newC = c - weight[i]
        #     if newC >= 0:
        #         include = profit[i] + helper(i, newC)

        #     cache[(i, c)] = max(include, skip)

        #     return cache[(i, c)]

        # return helper(0, capacity)