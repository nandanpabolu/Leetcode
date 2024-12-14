from collections import deque

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        total_sum = 0 
        queue = deque((root, root.val))
        
        while queue:
            node, number = queue.popleft()
            
            if not root.left and not root.right:
                total_sum +=  number
                
            if root.left:
                queue.append((node.left, number * 10 + node.left.val))
            if root.right:
                queue.append((node.right, number * 10 + node.right.val))
        return total_sum 
        