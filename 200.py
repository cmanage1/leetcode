class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs whenever we encounter a 1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def bfs(i, j):
            q = deque()
            q.append((i,j))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if new_r in range(ROWS) and new_c in range(COLS):
                        if grid[new_r][new_c] == "1":
                            q.append((new_r, new_c))
                            grid[new_r][new_c] = "0"


        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    bfs(i, j)
                    res += 1

        return res
