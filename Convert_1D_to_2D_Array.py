import numpy as np

class Solution:
    def construct2DArray(self, original, m, n):
        # Check if the total number of elements matches m * n
        if len(original) != m * n:
            return []  
        
        # Use NumPy to reshape the 1D array into a 2D array
        arr2D = np.array(original).reshape(m, n)
        return arr2D.tolist()

# Example usage:
sol = Solution()
original = [1, 2, 3, 4, 5, 6]
m = 2
n = 3
print(sol.construct2DArray(original, m, n))
