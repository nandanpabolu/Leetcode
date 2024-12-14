class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = 0 
        closed_count = 0 
        
        for char in s:
            if char == '(':
                    open_count += 1 
            elif char == ')':
                if open_count > 0:
                    closed_count -= 1 
                else:
                    closed_count += 1 
        return open_count + closed_count
    
    # Time Complexity O(n)
    # Space Complexity O(n)