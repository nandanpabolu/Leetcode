from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        if not root:
            return True  # An empty tree is trivially Even-Odd
        
        # Initialize a queue for BFS (level-order traversal)
        queue = deque([root])
        level = 0  # Start from the root level (level 0)
        
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            prev_val = None  # Track the previous value at the current level
            
            for i in range(level_size):
                node = queue.popleft()
                
                # Check if the current level is even or odd
                if level % 2 == 0:
                    # Even level: node values must be odd and strictly increasing
                    if node.val % 2 == 0:
                        return False  # Node value is even, but it should be odd
                    if prev_val is not None and node.val <= prev_val:
                        return False  # Values must be strictly increasing
                else:
                    # Odd level: node values must be even and strictly decreasing
                    if node.val % 2 == 1:
                        return False  # Node value is odd, but it should be even
                    if prev_val is not None and node.val >= prev_val:
                        return False  # Values must be strictly decreasing
                
                # Update prev_val for the next node comparison
                prev_val = node.val
                
                # Add the left and right children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Move to the next level
            level += 1
        
        return True  # If all levels satisfy the conditions, return True
