class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        removed_elements = [nums.pop() for _ in range(k)]
        removed_elements.reverse()
        nums = removed_elements + nums

        return nums
