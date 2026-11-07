class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = dict()
        def path(r, c):
            nonlocal cache
            if r == (m-1) and c == (n-1):
                return 1
            if r == m or c == n:
                return 0
            if (r, c) in cache:
                return cache[(r, c)]
            cache[(r, c)] = path(r+1, c) + path(r, c+1)
            return cache[(r, c)]
        
        return path(0,0)