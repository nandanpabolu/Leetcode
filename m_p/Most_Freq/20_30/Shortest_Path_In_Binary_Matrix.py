from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        
        if grid[N-1][N-1] == 1 or grid[0][0] == 1:
            return -1
        
        if N == 1 and grid[0][0] == 0:
            return 1 
        
        queue = ([(0,0,1)])
        visited = set([(0,0)])
        
        directions = [[0,1],[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[-1,-1],[1,-1]]
        while queue:
            r,c,l = queue.popleft()
            
            if r == N-1 and c == N-1:
                return l
            
            for drr, drc in directions:
                n_r, n_c = drr + r , drc + c 
                
                if 0 <= n_r < N and 0 <= n_c < N and (n_c,n_r) not in visited and grid[n_r][n_c] == 0:
                    queue.append((n_r, n_c, l+1))
                    visited.add((n_r, n_c))
        return -1 
            
            
            
            