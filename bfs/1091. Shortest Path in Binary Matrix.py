# type: ignore

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        grid[0][0] = 1

        queue = Deque([(0, 0, 1)])

        while queue:
            r, c, step = queue.popleft()

            if r == n-1 and c == n-1:
                return step
            
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if n > r + i >= 0 and n > c + j >= 0 and grid[r + i][c + j] == 0:
                        grid[r + i][c + j] = 1
                        queue.append((r + i, c + j, step + 1))
        
        return -1