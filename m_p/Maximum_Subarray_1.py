from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Calculate the sum of the first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum

        # Slide the window through the array
        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]  # Add new element, remove the leftmost element
            max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is greater

        # Return the maximum average
        return max_sum / k
