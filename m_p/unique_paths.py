class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Dictionary to store results of subproblems
        memo = {}

        def dfs(x, y):
            # Base case: if we reach the bottom-right corner, there's one path
            if x == m - 1 and y == n - 1:
                return 1
            # If out of bounds, return 0
            if x >= m or y >= n:
                return 0
            # If the result for this cell is already computed, return it
            if (x, y) in memo:
                return memo[(x, y)]
            # Compute the result and store it in the memo
            memo[(x, y)] = dfs(x + 1, y) + dfs(x, y + 1)
            return memo[(x, y)]

        return dfs(0, 0)
