from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0  # Return 0 if the tree is empty
        
        total_sum = 0  # Initialize sum
        queue = deque([root])  # Use a queue to perform BFS
        
        # BFS traversal
        while queue:
            node = queue.popleft()  # Get the front node from the queue
            
            if node:
                # If the node's value is within the range, add it to the total_sum
                if low <= node.val <= high:
                    total_sum += node.val
                
                # If the node's value is greater than low, its left subtree may contain values in range
                if node.val > low:
                    queue.append(node.left)
                
                # If the node's value is less than high, its right subtree may contain values in range
                if node.val < high:
                    queue.append(node.right)
        
        return total_sum  # Return the final sum after processing all nodes
