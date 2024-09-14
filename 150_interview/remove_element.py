class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0  # Pointer to track the position of the non-val elements
        for j in range(len(nums)):
            if nums[j] != val:  # If the current element is not equal to val
                nums[i] = nums[j]  # Move it to the 'i' position
                i += 1  # Increment the index for the next non-val element
        return i  # Return the number of elements that are not equal to val
