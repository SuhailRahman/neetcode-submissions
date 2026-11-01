class Solution:
    def rob(self, nums: List[int]) -> int:
        # cache = [-1] * len(nums)
        arrLength = len(nums)
        if arrLength == 1:
            return nums[0]
        # cache = [0] * (arrLength + 1)
        # cache[1] = nums[0]
        rob1, rob2 = 0, 0
        for i in range(arrLength):
            tmp = max(rob1 + nums[i], rob2)
            rob1 = rob2
            rob2 = tmp
            # val = nums[i]
            # cache[i+1] = max(val + cache[i-1], cache[i])
        return rob2
        # return self.robb(nums, len(nums) - 1, cache)
        # arrLength = len(nums)
        # if arrLength < 1:
        #     return 0
        # if arrLength in self.cache:
        #     return self.cache[arrLength]
        # res = max(nums[-1] + self.rob(nums[:arrLength-2]), self.rob(nums[:arrLength-1]))
        # self.cache[arrLength] = res
        # return res

    # def robb(self, nums, i, cache):
    #     # if i < 0:
    #     #     return 0
    #     # if cache[i] > 0:
    #     #     return cache[i]
    #     # res = max(nums[i] + self.robb(nums, i-2, cache), self.robb(nums, i-1, cache))
    #     # cache[i] = res
    #     # return res

