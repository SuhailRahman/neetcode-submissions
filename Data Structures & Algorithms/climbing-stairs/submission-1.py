class Solution:
    cache = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n-2) + self.climbStairs(n-1) 
        return self.cache[n]