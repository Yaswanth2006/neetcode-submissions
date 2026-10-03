class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        pos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visit.add((r, c))
        dist = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                for x, y in pos:
                    if (min(r + x, c + y) < 0 or r + x == ROWS or c + y == COLS or grid[r + x][c + y] == -1 or (r + x, c + y) in visit):
                        continue
                    queue.append((r + x, c + y))
                    visit.add((r + x, c + y))
            dist += 1