class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        # dp = [[1] * (n) for _ in range(n)]
        # print(dp)
        # return 1
        cache = dict()
        def lIS(i, prevNum):
            nonlocal cache
            if i == n:
                return 0
            if (i, prevNum) in cache:
                return cache[(i, prevNum)] 
            res = lIS(i+1, prevNum)
            if prevNum == float("-inf") or nums[i] > prevNum:
                res = max(res, lIS(i+1, nums[i]) + 1)
            cache[(i, prevNum)] = res
            return cache[(i, prevNum)]
        return lIS(0, float("-inf"))
        # maxLen = 0
        # for idx, num in enumerate(nums):
        #     maxLen = max(maxLen, lIS(idx+1, num))
        
        # return maxLen

