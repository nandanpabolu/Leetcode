class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openCount = 0 
        closedCount = 0 
        for char in s:
            if char == '(':
                openCount += 1
            elif char == ')':
                if openCount > 0:
                    openCount -= 1
                else:
                    closedCount += 1
        
        return openCount + closedCount
