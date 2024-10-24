class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # Iterate through the matrix (excluding the last row and last column)
        for i in range(len(matrix) - 1):
            for j in range(len(matrix[0]) - 1):
                # Check if the current element is equal to the one on its bottom-right diagonal
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        # If all diagonals have the same elements, return True
        return True

