class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific_set = set()
        atlantic_set = set()
        
        def dfs(r, c, visited, prev_height):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or prev_height > heights[r][c]:
                return
            
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        for i in range(ROWS):
            # pacific_set.add((i, 0))
            dfs(i, 0, pacific_set, heights[i][0])
            dfs(i, COLS-1, atlantic_set, heights[i][COLS-1])
            # atlantic_set.add((i, COLS-1))

        for j in range(COLS):
            # pacific_set.add((0, j))
            dfs(0, j, pacific_set, heights[0][j])
            dfs(ROWS-1, j, atlantic_set, heights[ROWS-1][j])
            # atlantic_set.add((ROWS-1, j))

        # for row, col in pacific_set:
        #     dfs(row, col, pacific_set, heights[row][col])

        # for row, col in atlantic_set:
        #     dfs(row, col, atlantic_set, heights[row][col])
        res = []

        for r, c in pacific_set:
            if (r, c) in atlantic_set:
                res.append([r, c])
        
        return res