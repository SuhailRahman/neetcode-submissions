class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        cache = dict()
        def maxAmount(i):
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i] + maxAmount(i+2), maxAmount(i+1))
            return cache[i]
        
        return maxAmount(0)