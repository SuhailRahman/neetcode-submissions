class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_lookup_table = {nums[0]: 0}
        for idx in range(1, len(nums)):
            second = nums[idx]
            first = target - second
            if first in hash_lookup_table:
                return [hash_lookup_table[first], idx]
            hash_lookup_table[second] = idx
            