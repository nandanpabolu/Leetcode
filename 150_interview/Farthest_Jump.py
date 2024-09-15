class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0  # Tracks the farthest index we can reach
        
        for i in range(len(nums)):
            if i > farthest:  # If the current index is beyond the farthest we can reach
                return False
            farthest = max(farthest, i + nums[i])  # Update the farthest we can reach
        
        return True  # If the loop completes, we can reach the end
