class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = float("-inf")
        curMax = 1
        curMin = 1

        for num in nums:
            if num == 0:
                curMax = 1
                curMin = 1
                res = max(res, 0)
                continue
            # print("Starting", curMax, curMin)
            prevMax = curMax
            curMax = max(num, curMax*num, curMin*num)
            curMin = min(num, curMin*num, prevMax*num)
            # print("Ending", curMax, curMin)
            res = max(res, curMax)
        return res
