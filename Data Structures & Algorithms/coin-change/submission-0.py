class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        cache = dict()
        def minCount(i, k):
            if k == 0:
                return 0
            if k < 0 or i == n:
                return float("inf")
            if (i, k) in cache:
                return cache[(i,k)]
            cache[(i,k)] = min(1 + minCount(i, k-coins[i]), minCount(i+1, k))
            return cache[(i,k)]
        
        res = minCount(0, amount)
        return res if res != float("inf") else -1