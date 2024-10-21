# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total_sum = 0 
        stack = [root]

        if not root:
            return 0  # Return 0 if the tree is empty
            
        while stack:
            node = stack.pop()
            if node:
                # Add the node's value if it's within the range [low, high]
                if low <= node.val <= high:
                    total_sum += node.val
                
                # If the current node's value is greater than low, explore the left subtree
                if node.val > low:
                    stack.append(node.left)
                
                # If the current node's value is less than high, explore the right subtree
                if node.val < high:
                    stack.append(node.right)
        
        return total_sum
