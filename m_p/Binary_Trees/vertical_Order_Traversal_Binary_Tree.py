from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to store nodes grouped by columns
        column_table = defaultdict(list)
        
        # BFS queue to store (node, row, col)
        queue = deque([(root, 0, 0)])
        
        # Perform BFS traversal
        while queue:
            node, row, col = queue.popleft()
            
            if node:
                # Append (row, value) to the respective column
                column_table[col].append((row, node.val))
                
                # Add left and right children to the queue with updated positions
                queue.append((node.left, row + 1, col - 1))
                queue.append((node.right, row + 1, col + 1))
        
        # Sort columns by keys (column index)
        sorted_columns = sorted(column_table.keys())
        
        result = []
        for col in sorted_columns:
            # Sort nodes within the column by (row, value)
            column_table[col].sort(key=lambda x: (x[0], x[1]))
            # Append only the values to the result
            result.append([val for _, val in column_table[col]])
        
        return result
