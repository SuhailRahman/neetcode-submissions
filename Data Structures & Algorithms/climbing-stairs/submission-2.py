class Solution:
    cache = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        for i in range(3, n+1):
            self.cache[i] = self.cache[i-1] + self.cache[i-2]
        return self.cache[n]