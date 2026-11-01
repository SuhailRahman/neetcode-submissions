class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        pre_prod_list = []
        pre_prod = 1
        for num in nums:
            pre_prod *= num
            pre_prod_list.append(pre_prod)
            
        post_prod_list = [1] * length
        post_prod = 1
        for i in range(length-1, -1, -1):
            post_prod *= nums[i]
            post_prod_list[i] *= post_prod
        
        res_list = []
        for i in range(length):
            prev_prod = pre_prod_list[i-1] if i-1 >= 0 else 1
            post_prod = post_prod_list[i+1] if i+1 < length else 1
            res_list.append(prev_prod*post_prod)
        
        return res_list