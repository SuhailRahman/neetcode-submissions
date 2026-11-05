class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # cache = dict()
        # def minCount(i, k):
        #     if k == 0:
        #         return 0
        #     if k < 0 or i == n:
        #         return float("inf")
        #     if (i, k) in cache:
        #         return cache[(i,k)]
        #     cache[(i,k)] = min(1 + minCount(i, k-coins[i]), minCount(i+1, k))
        #     return cache[(i,k)]
        
        # res = minCount(0, amount)
        # return res if res != float("inf") else -1
        k = amount
        dp = [[float('inf')] * (k+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(n-1, -1, -1):
            for k in range(k+1):
                dp[i][k] = dp[i+1][k]
                if (k-coins[i]) >= 0:
                    dp[i][k] = min(dp[i][k], 1+dp[i][k-coins[i]])
        
        return dp[0][k] if dp[0][k] != float("inf") else -1
