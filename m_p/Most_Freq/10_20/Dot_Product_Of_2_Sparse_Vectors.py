# Time Complexity: O(n + min(K1,k2)) K1 and K2 are number of non zero elements in v1 and v2 
# Space Complexity: O(k1 + k2)
class SparseVector:
   
    def __init__(self, nums: List[int]):
        self.nums = []
        for i, num in enumerate(nums):
            self.nums.append((i,num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        i = j = 0 
        result = 0
        while i < len(self.nums) and j < len(vec.nums):
            i_idx, i_val = self.nums[i]
            j_idx, j_val = vec.nums[j]

            if i_idx == j_idx:
                result += i_val * j_val

                i += 1 
                j += 1 

            elif i_idx < j_idx:
                i += 1 

            else:
                j += 1

        return result        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)