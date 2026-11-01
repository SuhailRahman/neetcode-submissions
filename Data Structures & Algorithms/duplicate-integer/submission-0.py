class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_nums_set = set()
        for num in nums:
            if num in distinct_nums_set:
                return True
            distinct_nums_set.add(num)
        return False
        