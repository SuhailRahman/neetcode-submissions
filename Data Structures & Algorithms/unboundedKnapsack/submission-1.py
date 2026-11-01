class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        cache = dict()
        def helper(i, c):
            if i == n:
                return 0
            if (i, c) in cache:
                return cache[(i, c)]
            skip = helper(i+1, c)
            include = 0

            newC = c - weight[i]
            if newC >= 0:
                include = profit[i] + helper(i, newC)
            cache[(i, c)] = max(include, skip)
            return cache[(i, c)]
        return helper(0, capacity)