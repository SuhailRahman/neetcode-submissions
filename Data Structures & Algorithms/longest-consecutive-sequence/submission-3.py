class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums) == 0:
        #     return 0
        # max_count = 1
        # nums.sort()
        # i = 1
        # n = len(nums)
        # while i < n:
        #     cur_count = 1
        #     j = i
        #     while j < n and (nums[j] == nums[j-1] or nums[j] == (1+nums[j-1])):
        #         if nums[j] == (1+nums[j-1]):
        #             cur_count += 1
        #         j += 1
        #     max_count = max(max_count, cur_count)
        #     i = j+1
        # return max_count
        
        n = len(nums)
        if n == 0:
            return 0
        
        hashset = set(nums)
        
        max_count = 1
        for num in nums:
            if (num-1) not in hashset:
                cur_count = 0
                cur_num = num
                while cur_num in hashset:
                    cur_count += 1
                    cur_num += 1
                max_count = max(max_count, cur_count)
        return max_count
                


