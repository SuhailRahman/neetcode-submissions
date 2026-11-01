class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        i = 0
        res = []
        while i < n:
            l = i+1
            r = n-1
            while l<r: 
                sum = nums[i] + nums[l] + nums[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while r > l and nums[r] == nums[r-1]:
                        r -= 1
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    l += 1
                    r -= 1
            while (i+1) < n and nums[i] == nums[i+1]:
                i += 1
            i += 1
            
                    
        return res