class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)

        def helper(i, c):
            if i == n:
                return 0
            
            skip = helper(i+1, c)
            include = 0

            newC = c - weight[i]
            if newC >= 0:
                include = profit[i] + helper(i, newC)
            
            return max(include, skip)
        return helper(0, capacity)