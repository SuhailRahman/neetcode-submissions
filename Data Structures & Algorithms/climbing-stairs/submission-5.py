class Solution:
    def climbStairs(self, n: int) -> int:
        # cache = dict()
        # def countStairs(n):
        #     nonlocal cache
        #     if n < 0:
        #         return 0
        #     if n == 0:
        #         return 1
        #     if n in cache:
        #         return cache[n]
        #     cache[n] = countStairs(n-1) + countStairs(n-2)
        #     return cache[n]
        # return countStairs(n)
        if n < 0:
            return 0
        if n == 0:
            return 1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]