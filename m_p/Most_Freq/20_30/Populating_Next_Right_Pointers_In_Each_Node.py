from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None  # Handle empty tree

        # Use a queue for level-order traversal
        queue = deque([root])

        while queue:
            level_size = len(queue)
            prev = None  # Reset previous node for each level

            for _ in range(level_size):
                node = queue.popleft()

                # Connect the previous node to the current node
                if prev:
                    prev.next = node
                prev = node

                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Ensure the last node in the level points to None
            prev.next = None

        return root