class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        islands = 0
        from collections import deque
        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visit.add((r, c))
            pos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            while queue:
                rr, cc = queue.popleft()
                for x, y in pos:
                    if (min(x + rr, y + cc) < 0 or x + rr == ROWS 
                    or y + cc == COLS or grid[x + rr][y + cc] == '0'
                    or (x + rr, y + cc) in visit):
                        continue
                    queue.append((x + rr, y + cc))
                    visit.add((x + rr, y + cc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands