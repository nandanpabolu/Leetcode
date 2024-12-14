class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        
        Output = []
        max_height = 0 
        
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > max_height:
                Output.append(i)
                max_height = heights[i]
        return Output[::-1]
                
                
        
# Time Complexity is O(n)
# Space Complexity is O(K) where K are number of ocean facing buildings

