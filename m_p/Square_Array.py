class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)  # Correctly initialize the result list
        left, right = 0, len(nums) - 1
        pos = len(nums) - 1

        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2

            if left_sq > right_sq:
                result[pos] = left_sq
                left += 1
            else:  # Handles both `right_sq > left_sq` and `right_sq == left_sq`
                result[pos] = right_sq
                right -= 1
            pos -= 1

        return result
