class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        from collections import deque
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        count = 0
        pos = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        #adding it to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visit.add((r, c))
                    queue.append((r, c))
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = count
                for x, y in pos:
                    if (min(r + x, c + y) < 0 or ROWS == r + x or COLS == c + y or (r + x, c + y) in visit or grid[r + x][c + y] == -1):
                        continue
                    queue.append((r + x, c + y))
                    visit.add((r + x, c + y))
            count += 1
                
