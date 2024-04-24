class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # another dfs
        # this needs to have backtracking
        visited = set()
        
        def dfs(r, c, currIndex):
            if currIndex == len(word):
                return True
            if r not in range(0, len(word)) or c not in range(0, len(word[0])) or word[currIndex] != board[r][c] or (r,c) in visited:
                return False

            visited.add((r,c))
            res = (
                dfs(r+1, c, currIndex+1) or
                dfs(r-1, c, currIndex+1) or
                dfs(r, c+1, currIndex+1) or
                dfs(r, c+1, currIndex+1)
            )
            visited.remove((r, c))
            return res
            

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
