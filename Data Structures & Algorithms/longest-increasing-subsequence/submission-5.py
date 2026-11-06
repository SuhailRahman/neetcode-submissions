class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # cache = dict()
        # def lIS(i, prevNum):
        #     nonlocal cache
        #     if i == n:
        #         return 0
        #     if (i, prevNum) in cache:
        #         return cache[(i, prevNum)] 
        #     res = lIS(i+1, prevNum)
        #     if prevNum == float("-inf") or nums[i] > prevNum:
        #         res = max(res, lIS(i+1, nums[i]) + 1)
        #     cache[(i, prevNum)] = res
        #     return cache[(i, prevNum)]
        # return lIS(0, float("-inf"))

        dp = [[0] * (n+1) for _ in range(n+1)]

        for i in range(n-1, -1, -1):
            for j in range(n, -1, -1):
                dp[i][j] = dp[i+1][j]
                if j == (n) or nums[i] > nums[j]:
                    dp[i][j] = max(dp[i][j], dp[i+1][i] + 1)

        # print(dp)
        return dp[0][n]


