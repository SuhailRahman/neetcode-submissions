class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # cache = dict()
        # def jump(i):
        #     if i >= (n-1):
        #         return True
        #     if i in cache:
        #         return cache[i]
        #     if nums[i] == 0:
        #         return False
        #     res = False
        #     for j in range(1, nums[i]+1):
        #         if jump(i+j):
        #             res = True
        #             break
        #     cache[i] = res
        #     return cache[i]

        # return jump(0)

        dp = [False] * (n)
        dp[n-1] = True
        for i in range(n-2, -1, -1):
            if nums[i] == 0:
                dp[i] = False
            for j in range(i+1, i+nums[i]+1):
                if dp[j]:
                    dp[i] = True
                    break

        
        return dp[0]