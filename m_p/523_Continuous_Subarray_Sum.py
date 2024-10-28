class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0: -1}  # Store remainder as key and index as value
        prefix_sum = 0  # Initialize prefix sum to 0

        for i, num in enumerate(nums):
            # Update the prefix sum by adding the current number
            prefix_sum += num

            # If k is not 0, calculate prefix_sum mod k
            if k != 0:
                prefix_sum %= k

            # If the remainder has been seen before
            if prefix_sum in remainder_map:
                # Check if the subarray is at least of size 2
                if i - remainder_map[prefix_sum] > 1:
                    return True
            else:
                # Store the first occurrence of this remainder
                remainder_map[prefix_sum] = i
        
        return False
