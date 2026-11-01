class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = 0
        second = 0
        res = 0
        for stair in cost:
            temp = stair + min(first, second)
            first = second
            second = temp
        return min(second, first)