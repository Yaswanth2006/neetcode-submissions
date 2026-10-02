class Solution:
    from collections import deque
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        
        def bfs(r, c):
            queue = deque()
            visit.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for x, y in directions:
                    if (min(row + x, col + y) < 0 or row + x == ROWS or col + y == COLS or grid[row + x][col + y] == '0' or (row + x, col + y) in visit):
                        continue
                    queue.append((row + x, col + y))
                    visit.add((row + x, col + y))
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands