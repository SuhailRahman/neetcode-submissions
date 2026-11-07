class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        max_sum_ending = 0
        for num in nums:
            max_sum_ending = max(0, max_sum_ending)
            max_sum_ending += num
            res = max(res, max_sum_ending)
        
        return res