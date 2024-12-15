class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        
        def dfs(x,y):
            
            if x == m-1 and y == n-1:
                return 1
            if x >= m or y >= n:
                return 0 
            
            if (x,y) in memo:
                return memo[(x,y)]
            
            memo[(x,y)] = dfs(x+1 , y) + dfs(x, y + 1)
            return memo[(x+y)]
        return dfs(0,0)
    
# Time Complexity O(m+n)
# Space Complexity 0(M*n)
