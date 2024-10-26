class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)  # size of the grid
        island_index = 2  # start indexing islands from 2
        island_area = {}  # store the area of each island

        def dfs(x, y, index):
            if 0 <= x < n and 0 <= y < n and grid[x][y] == 1:  # Fix typo here
                grid[x][y] = index  # Mark the grid cell with the island index
                area = 1  # Start with area = 1 for this cell
                # Recursively visit all neighboring cells (up, down, left, right)
                area += dfs(x + 1, y, index)
                area += dfs(x - 1, y, index)
                area += dfs(x, y + 1, index)
                area += dfs(x, y - 1, index)
                return area  # return the total area of this island
            return 0

        # Step 1: Find all islands and compute their areas
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:  # Found a new island
                    area = dfs(i, j, island_index)  # Compute the area of the island
                    island_area[island_index] = area  # Store the area
                    island_index += 1  # Increment island index for the next island

        # Initialize the max_area with the largest island found so far
        max_area = max(island_area.values(), default=0)

        # Step 2: Try to convert a 0 into a 1 and connect neighboring islands
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:  # Only interested in 0 cells
                    seen = set()  # To keep track of unique neighboring islands
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < n and 0 <= y < n and grid[x][y] > 1:
                            seen.add(grid[x][y])  # Add the neighboring island's index

                    # Calculate the new area by converting this 0 to 1 and connecting islands
                    new_area = 1  # The new 1 cell we created
                    for index in seen:
                        new_area += island_area[index]  # Add the areas of the neighboring islands

                    # Update max_area with the largest possible island area
                    max_area = max(max_area, new_area)

        # If the grid is all 1's, max_area won't change, so return n * n
        return max_area if max_area != 0 else n * n
