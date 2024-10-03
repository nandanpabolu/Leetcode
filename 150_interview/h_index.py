from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # Step 1: Sort the citations in ascending order
        citations.sort()
        
        # Step 2: Initialize the counter (number of papers to check)
        n = len(citations)
        
        # Step 3: Traverse from the last (most citations) to the first (least citations)
        for i in range(n):
            # Number of papers with citations greater than or equal to the current paper's citation
            h_candidate = n - i  
            
            # Check if this is a valid h-index
            if citations[i] >= h_candidate:
                return h_candidate
        
        # If no valid h-index is found, return 0
        return 0
