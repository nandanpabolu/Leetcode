class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        
        j = 1  # Pointer for the next position to insert valid elements
        counter = 1  # We start by allowing one appearance of the first element
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                counter += 1
            else:
                counter = 1  # Reset counter for a new number
            
            if counter <= 2:  # Allow the element to be inserted if it appears at most twice
                nums[j] = nums[i]
                j += 1
        
        return j  # 'j' is the length of the array without extra duplicates
