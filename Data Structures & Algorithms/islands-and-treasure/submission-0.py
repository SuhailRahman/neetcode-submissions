from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        visited = set()

        ROWS, COLS = len(grid), len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    visited.add((i, j))
        def addRooms(r, c):
            if r == ROWS or c == COLS or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == -1:
                return
            queue.append([r, c])
            visited.add((r, c))
        dist = 0
        while len(queue) > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                addRooms(r+1, c)
                addRooms(r-1, c)
                addRooms(r, c+1)
                addRooms(r, c-1)
            dist += 1