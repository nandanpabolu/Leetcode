from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # Ensure bounds and evaluate slope
            if arr[mid] < arr[mid + 1]:  # Check if in the ascending part
                low = mid + 1
            else:  # Otherwise, in the descending part or at the peak
                high = mid
        
        # At the end of the loop, low == high, pointing to the peak
        return low