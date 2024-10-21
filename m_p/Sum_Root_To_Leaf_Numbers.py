from collections import deque

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0  # Return 0 instead of []
        
        total_sum = 0
        queue = deque([(root, root.val)])  # Initialize the queue with the root and its value
        
        while queue:
            node, current_number = queue.popleft()
            
            # Check if it's a leaf node (both left and right children are None)
            if not node.left and not node.right:
                total_sum += current_number  # Add the current path number to total sum
            
            # If there is a left child, add it to the queue with the updated number
            if node.left:
                queue.append((node.left, current_number * 10 + node.left.val))
            
            # If there is a right child, add it to the queue with the updated number
            if node.right:
                queue.append((node.right, current_number * 10 + node.right.val))
        
        return total_sum  # Return the final total sum of all root-to-leaf numbers
