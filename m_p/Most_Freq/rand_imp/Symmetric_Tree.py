from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:  # An empty tree is symmetric
            return True
        
        # Initialize a queue for BFS
        queue = deque([(root.left, root.right)])
        
        while queue:
            left, right = queue.popleft()
            
            # Both nodes are None (symmetric)
            if not left and not right:
                continue
            
            # If one of them is None, or the values are not equal, return False
            if not left or not right or left.val != right.val:
                return False
            
            # Add children in a mirrored order
            queue.append((left.left, right.right))  # Left subtree's left and right subtree's right
            queue.append((left.right, right.left))  # Left subtree's right and right subtree's left
        
        return True
    
# Time Complexity is O(w)
# Space Complexity is O(h)