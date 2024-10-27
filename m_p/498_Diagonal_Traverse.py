from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        # Check for an empty matrix
        if not mat or not mat[0]:
            return []
        
        # Get the dimensions of the matrix
        m, n = len(mat), len(mat[0])
        
        # Result array to store the diagonal traversal
        result = []
        
        # `up` indicates the direction of the traversal (True for up, False for down)
        up = True
        
        # Start from the top-left corner of the matrix
        row, col = 0, 0
        
        # Traverse through the matrix until we get all elements
        while len(result) < m * n:
            result.append(mat[row][col])
            
            if up:
                # If moving upwards diagonally
                if col == n - 1:  # If at the last column, move down to the next row
                    row += 1
                    up = False
                elif row == 0:  # If at the first row, move to the next column
                    col += 1
                    up = False
                else:
                    # Move diagonally up
                    row -= 1
                    col += 1
            else:
                # If moving downwards diagonally
                if row == m - 1:  # If at the last row, move to the next column
                    col += 1
                    up = True
                elif col == 0:  # If at the first column, move to the next row
                    row += 1
                    up = True
                else:
                    # Move diagonally down
                    row += 1
                    col -= 1
        
        # Return the result array containing the diagonal traversal
        return result
