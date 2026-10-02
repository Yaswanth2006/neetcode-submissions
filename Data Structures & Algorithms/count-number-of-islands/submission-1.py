class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        def bfs(r, c):
            queue = deque()
            visit.add((r, c))
            queue.append((r, c))
            while queue:
                ra, ca = queue.popleft()
                pos = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for x, y in pos:
                    if (min(ra + x, ca + y)) < 0 or ra + x == ROWS or ca + y == COLS or grid[ra + x][ca + y] == '0' or (ra + x, ca + y) in visit:
                        continue
                    queue.append((ra + x, ca + y))
                    visit.add((ra + x, ca + y))
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1
        return islands
                