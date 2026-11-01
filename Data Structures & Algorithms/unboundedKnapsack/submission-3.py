class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        preRow = [0] * (capacity+1)

        for i in range(1, n+1):
            curRow = [0] * (capacity+1)
            for j in range(1, capacity+1):
                skip = preRow[j]
                include = 0
                if j - weight[i-1] >= 0 :
                    include = profit[i-1] + curRow[j - weight[i-1]]
                curRow[j] = max(include, skip)
            preRow = curRow
        return preRow[capacity]

        # cache = dict()
        # def helper(i, c):
        #     if i == n:
        #         return 0
        #     if (i, c) in cache:
        #         return cache[(i, c)]

        #     skip = helper(i+1, c)
        #     include = 0

        #     newC = c - weight[i]
        #     if newC >= 0:
        #         include = profit[i] + helper(i, newC)

        #     cache[(i, c)] = max(include, skip)

        #     return cache[(i, c)]

        # return helper(0, capacity)