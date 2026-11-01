class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        first = 1
        second = 2
        final = 0
        for i in range(3, n+1):
            final = first + second
            first = second
            second = final
        return final