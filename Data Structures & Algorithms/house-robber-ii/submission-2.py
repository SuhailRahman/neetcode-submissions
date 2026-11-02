class Solution:
    def rob(self, nums: List[int]) -> int:
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]
        def maxAmount(i, n):
            nonlocal cache
            if i >= n:
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i] + maxAmount(i+2, n), maxAmount(i+1, n))
            return cache[i]
        cache = dict()
        exclude_last = maxAmount(0, nums_len-1)
        cache = dict()
        exclude_first = maxAmount(1, nums_len)
        return max(exclude_last, exclude_first)