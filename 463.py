from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            q = deque([(i, j)])
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            perim = 4
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c  = dr+r, dc+c

                    if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 1:
                        perim -= 1
                        perim += 3
                        q.append((new_r, new_c))
                        grid[new_r][new_c] = 0

            return perim

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = dfs(i, j)

        return res
