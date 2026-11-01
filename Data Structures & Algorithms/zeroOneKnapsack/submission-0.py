class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        def helper(i, c, profitSF):
            if c == 0 or i == n:
                return profitSF
            if weight[i] <= c:
                return max(helper(i+1, c - weight[i], profitSF + profit[i]), helper(i+1, c, profitSF))
            else:
                return helper(i+1, c, profitSF)
        return helper(0, capacity, 0)