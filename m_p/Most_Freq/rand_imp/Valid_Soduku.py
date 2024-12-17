from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use sets to track seen numbers in rows, columns, and boxes
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for i in range(9):  # Iterate through each row
            for j in range(9):  # Iterate through each column
                num = board[i][j]
                
                if num == '.':  # Ignore empty cells
                    continue
                
                # Check if the number is already in the current row
                if num in rows[i]:
                    return False
                rows[i].add(num)
                
                # Check if the number is already in the current column
                if num in cols[j]:
                    return False
                cols[j].add(num)
                
                # Check if the number is in the current 3x3 sub-box
                box_index = (i // 3) * 3 + (j // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)
        
        return True