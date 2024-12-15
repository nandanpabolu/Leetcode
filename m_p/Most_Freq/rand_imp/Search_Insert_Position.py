from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:  # Use <= to handle edge cases
            mid = (low + high) // 2
            if nums[mid] == target:  # Found the target
                return mid
            elif nums[mid] < target:  # Target is in the right half
                low = mid + 1
            else:  # Target is in the left half
                high = mid - 1

        # If target is not found, `low` will be the insertion point
        return low
    
    # Binary search time complexity mentiined O(log n)
    # Space Complexity is O(1) Fixed variables