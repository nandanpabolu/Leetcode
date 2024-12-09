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
            return 0 
        
        total_sum = 0  # Initialize sum variable
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node:
                if low <= node.val <= high:
                    total_sum += node.val  # Add node value to the sum
                
                if node.val > low:
                    queue.append(node.left)  # Explore left subtree if node value > low
                
                if node.val < high:
                    queue.append(node.right)  # Explore right subtree if node value < high
        
        return total_sum
    
    # Time complecity O(n)