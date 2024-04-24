import collections

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # instead of visited set, make 1s = 0
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            grid[i][j] = 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            area = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    for dr, dc in directions:
                        new_r, new_c = dr+r, dc+c
                        if new_r in range(ROWS) and new_c in range(COLS) and grid[new_r][new_c] == 1:
                            area += 1
                            q.append((new_r, new_c))
                            grid[new_r][new_c] = 0 # mark as visited
            return area

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(bfs(r, c), maxArea)
        return maxArea
