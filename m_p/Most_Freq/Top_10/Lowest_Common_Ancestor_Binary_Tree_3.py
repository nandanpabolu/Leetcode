"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_seen = p
        q_seen = q 
        
        while p_seen != q_seen:
            p_seen = p_seen.parent if p_seen else q 
            q_seen = q_seen.parent if q_seen else p 
            
        return p_seen
    