class Solution:
    # visited = []
    # cache = []
    def rob(self, nums: List[int]) -> int:
        arrLength = len(nums)
        if arrLength == 1:
            return nums[0]
        if arrLength == 2:
            return max(nums[0], nums[1])
        # Top down approach with memoization
        # def helper(nums, arrLen, cache):
        #     if arrLen < 1:
        #         return 0
        #     if cache[arrLen-1]:
        #         return cache[arrLen-1]
        #     res = max(nums[arrLen - 1] + helper(nums, arrLen-2, cache), helper(nums, arrLen-1, cache))
        #     cache[arrLen-1] = res
        #     return cache[arrLen-1]
        # return max(helper(nums[:arrLength-1], arrLength-1, [0] * (arrLength-1)), helper(nums[1:], arrLength-1, [0] * (arrLength-1)))
        # DP Bottom up approach
        def helper(nums):
            cache = [0] * len(nums)
            cache[0] = nums[0]
            cache[1] = max(nums[0], nums[1])
            # first = 0
            # second = 0
            res = 0
            for index in range(2, len(nums)):
                cache[index] = max(nums[index] + cache[index-2], cache[index-1])
            return cache[-1]
        return max(helper(nums[:-1]), helper(nums[1:]))
        

    #     arrLength = len(nums)
    #     if arrLength == 1:
    #         return nums[0]
    #     self.visited = [0] * arrLength
    #     self.cache = [0] * (arrLength+1)
    #     self.robb(nums, len(nums))
    #     return self.cache[-1]

    # def robb(self, nums, arrLength):
    #     if arrLength < 1 or (arrLength == 1 and self.visited[-1] == 1):
    #         return 0
    #     if self.cache[arrLength]:
    #         return self.cache[arrLength]
    #     if arrLength == len(nums):
    #         self.visited[-1] = 1
    #     left = nums[arrLength - 1] + self.robb(nums, arrLength-2)
    #     if arrLength == len(nums):
    #         self.visited[-1] = 0
    #     right = self.robb(nums, arrLength-1)
    #     res = max(left, right)
    #     self.cache[arrLength] = res
    #     return self.cache[arrLength]