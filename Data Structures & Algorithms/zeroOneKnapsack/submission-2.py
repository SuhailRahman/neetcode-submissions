class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)

        dp = [[0] * (capacity + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = 0
        
        for i in range(capacity+1):
            if weight[0] <= i:
                dp[0][i] = profit[0]
        for i in range(1, n):
            for j in range(1, capacity+1):
                if weight[i] <= j:
                    dp[i][j] = max(profit[i] + dp[i-1][j-weight[i]], dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        print(dp)
        return dp[n-1][capacity]

        # cache = dict()
        # def helper(i, c):
        #     if c == 0 or i == n:
        #         return 0
        #     if (i, c) in cache:
        #         return cache[(i ,c)]
        #     if weight[i] <= c:
        #         cache[(i ,c)] = max(profit[i] + helper(i+1, c - weight[i]), helper(i+1, c))
        #     else:
        #         cache[(i ,c)] = helper(i+1, c)
        #     return cache[(i ,c)]
        
        # return helper(0, capacity)
        