class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_lookup_table = {}
        for idx, second in enumerate(nums):
            first = target - second
            if first in hash_lookup_table:
                return [hash_lookup_table[first], idx]
            hash_lookup_table[second] = idx
            