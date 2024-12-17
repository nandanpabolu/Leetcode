import heapq
import math
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Convert the list to a max-heap by negating values
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        # Perform the operation for k seconds
        for _ in range(k):
            # Extract the richest pile (largest number of gifts)
            largest_pile = -heapq.heappop(max_heap)
            
            # Calculate the number of gifts to leave behind
            remaining_gifts = math.floor(math.sqrt(largest_pile))
            
            # Push the remaining gifts back into the heap
            heapq.heappush(max_heap, -remaining_gifts)
        
        # Calculate the total remaining gifts
        return -sum(max_heap)
    
# Time Complexity is O(n + K log(n))
# Space Complexity is O(n)