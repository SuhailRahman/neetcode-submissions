class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums_len = len(nums)
        # if nums_len == 1:
        #     return nums[0]
        # def maxAmount(i, n):
        #     nonlocal cache
        #     if i >= n:
        #         return 0
        #     if i in cache:
        #         return cache[i]
        #     cache[i] = max(nums[i] + maxAmount(i+2, n), maxAmount(i+1, n))
        #     return cache[i]
        # cache = dict()
        # exclude_last = maxAmount(0, nums_len-1)
        # cache = dict()
        # exclude_first = maxAmount(1, nums_len)
        # return max(exclude_last, exclude_first)
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp1[1] = nums[0]
        dp2[1] = nums[1]
        for i in range(2, n):
            dp1[i] = max(nums[i-1] + dp1[i-2], dp1[i-1])
            dp2[i] = max(nums[i] + dp2[i-2], dp2[i-1])
        # print(dp1, dp2)
        return max(dp1[n-1], dp2[n-1])

