from collections import defaultdict
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)

        # Group elements by diagonals
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                # Append elements in reverse order (to simulate bottom-to-top)
                diagonals[i + j].append(nums[i][j])

        result = []
        # Traverse diagonals in sorted order
        for diagonal in sorted(diagonals.keys()):
            # Add the diagonal elements in reverse order
            result.extend(reversed(diagonals[diagonal]))
        
        return result
