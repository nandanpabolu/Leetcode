class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        removed_elements = [nums.pop() for _ in range(k)]
        removed_elements.reverse()
        nums = removed_elements + nums

        return nums

"this code has an issue concerning reassigning nums, turns out reassigning nums creates a different object of nums and affects function calling due to which i cant, what are poissible ways exist ? let me explore, however this code has been uploaded just for the sake of version history."