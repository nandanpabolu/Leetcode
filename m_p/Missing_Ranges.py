class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        output = []

        # If nums is empty, the whole range [lower, upper] is missing
        if not nums:
            output.append([lower, upper])
            return output

        # If there is a gap before the first element in nums
        if nums[0] > lower:
            output.append([lower, nums[0]-1]) 

        # Check gaps between consecutive elements in nums
        for i in range(len(nums) - 1):
            if nums[i] + 1 < nums[i + 1]:
                output.append([nums[i] + 1, nums[i + 1] - 1])

        # If there is a gap after the last element in nums
        if nums[-1] < upper:
            output.append([nums[-1] + 1, upper])

        return output
