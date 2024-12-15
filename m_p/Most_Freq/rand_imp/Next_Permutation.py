class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Modify nums in-place to the next lexicographical permutation.
        If no such permutation exists, rearrange it to the lowest possible order.
        """
    
    pivot = None
    
    for i in range(len(nums) -1 , 0, -1):
        if nums[i] > nums[i - 1]:
            pivot = i - 1
            break
    else:
        nums.reverse()
        return
    
    swap = len(nums) - 1 
    while nums[pivot] >= nums[swap]:
        swap -= 1 
    
    nums[pivot], nums[swap] = nums[swap], nums[pivot]
    
    nums[pivot + 1:] = reversed(nums[pivot + 1:])
    return
     

# Time complecity is O(n)
# Space complexity yet to be determined