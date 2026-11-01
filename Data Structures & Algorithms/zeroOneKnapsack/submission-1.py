class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(weight)
        cache = dict()
        def helper(i, c):
            if c == 0 or i == n:
                return 0
            if (i, c) in cache:
                return cache[(i ,c)]
            if weight[i] <= c:
                cache[(i ,c)] = max(profit[i] + helper(i+1, c - weight[i]), helper(i+1, c))
            else:
                cache[(i ,c)] = helper(i+1, c)
            return cache[(i ,c)]
        
        return helper(0, capacity)
        