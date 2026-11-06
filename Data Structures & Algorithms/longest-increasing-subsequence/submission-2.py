class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        cache = dict()
        def lIS(i, prevNum):
            nonlocal cache
            if i == n:
                return 1
            if (i, prevNum) in cache:
                return cache[(i, prevNum)] 
            res = lIS(i+1, prevNum)
            if nums[i] > prevNum:
                res = max(res, lIS(i+1, nums[i]) + 1)
            cache[(i, prevNum)] = res
            return cache[(i, prevNum)]
        maxLen = 0
        for idx, num in enumerate(nums):
            maxLen = max(maxLen, lIS(idx+1, num))
        
        return maxLen

