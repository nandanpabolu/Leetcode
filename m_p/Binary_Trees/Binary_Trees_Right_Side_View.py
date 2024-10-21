from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []  # Corrected the return statement
        
        output = []  # List to store the rightmost node values
        queue = deque([root])  # Initialize the queue with the root node

        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            
            for i in range(level_size):
                node = queue.popleft()  # Dequeue the current node

                # If this is the last node in the current level, add its value to the result
                if i == level_size - 1:
                    output.append(node.val)
                
                # Add the left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                
                # Add the right child to the queue if it exists
                if node.right:
                    queue.append(node.right)
        
        return output  # Return the final result
