from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Step 1: Sort the input list to enable two-pointer traversal
        nums.sort()
        closest_sum = float('inf')  # Initialize the closest sum to a very large value

        # Step 2: Iterate through the list using the first pointer (i)
        for i in range(len(nums) - 2):  # -2 because we need at least 3 numbers
            left, right = i + 1, len(nums) - 1  # Initialize two pointers
            
            # Step 3: Move the left and right pointers towards each other
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]  # Calculate the current triplet sum
                
                # Step 4: Update closest_sum if the current sum is closer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Step 5: Move pointers based on comparison with target
                if current_sum < target:
                    left += 1  # Move left pointer to increase the sum
                elif current_sum > target:
                    right -= 1  # Move right pointer to decrease the sum
                else:
                    # If the exact target is found, return immediately
                    return closest_sum
        
        # Step 6: Return the closest sum found
        return closest_sum

#Time Complexity is O(n^2)
#Space Complexity is O(1)