from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]  # Return the indices of the two numbers
        
        return []  # Return an empty list if no solution is found
    
# Time Complexity for this approach is O(n^2)


#Approach 2 using hash map 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # To store indices of visited numbers
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i  # Store the index of the current number
        
        return []  # If no solution is found