class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def combinations(i, cur_comb, cur_sum):
            nonlocal res
            if i == n or cur_sum > target:
                return
            if cur_sum == target:
                res.append(cur_comb.copy())
                return
            
            cur_comb.append(nums[i])
            combinations(i, cur_comb, cur_sum + nums[i])

            cur_comb.pop()
            combinations(i+1, cur_comb, cur_sum)
        
        combinations(0, [], 0)
        return res