class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        max_height = 0
        
        # Traverse from right to left
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                result.append(i)
                # Update max_height only if the current building has an ocean view
                max_height = heights[i]
        
        # Return the result in left-to-right order
        return result[::-1]
