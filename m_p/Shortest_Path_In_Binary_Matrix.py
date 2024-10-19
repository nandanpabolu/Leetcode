from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        # If the starting or ending cell is blocked, return -1
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        
        # Initialize the queue and visited set
        q = deque([(0, 0, 1)])  # (row, col, path_length)
        visit = set([(0, 0)])
        
        # Directions for movement in 8 directions
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        
        # Breadth-First Search (BFS)
        while q:
            r, c, length = q.popleft()
            
            # If we've reached the bottom-right corner, return the path length
            if r == N - 1 and c == N - 1:
                return length
            
            # Explore all 8 directions
            for drr, drc in direct:
                new_r, new_c = r + drr, c + drc
                # Check if the new position is within bounds and not visited and not blocked
                if 0 <= new_r < N and 0 <= new_c < N and (new_r, new_c) not in visit and grid[new_r][new_c] == 0:
                    q.append((new_r, new_c, length + 1))
                    visit.add((new_r, new_c))
        
        # If no path exists, return -1
        return -1
