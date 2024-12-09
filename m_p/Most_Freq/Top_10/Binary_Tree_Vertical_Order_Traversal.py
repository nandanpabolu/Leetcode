from collections import defautdict, deque 
from typing import Optional,List 

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_map = defautdict(list)
        
        queue = deque([root, 0])
        
        while queue:
            
            node, col = queue.popleft()
            column_map[col].append(node.val)
            
            if node.left:
                queue.append([node.left, col-1])
            elif node.right:
                queue.append([node.right, col + 1])
            
        
        result = [column_map[col] for col in sorted(column_map.keys())]
        return result 