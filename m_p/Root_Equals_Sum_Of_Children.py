# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        # Check if the value of the root equals the sum of its children's values
        return root.left.val + root.right.val == root.val
