from typing import List
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]  # If distance is 0, return the target node value
        
        # Step 1: Build the graph
        graph = collections.defaultdict(list)
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
            
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)
        
        # Step 2: Perform BFS from the target node
        res = []
        visited = set([target])  # Mark the target as visited
        queue = collections.deque([(target, 0)])  # Start BFS with target node
        
        while queue:
            node, distance = queue.popleft()
            
            if distance == k:
                res.append(node.val)  # Add node value if the distance is k
            else:
                for neighbor in graph[node]:
                    if neighbor not in visited:  # Avoid revisiting nodes
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))
        
        return res

# Time Complexity: O(n) for graph construction + O(n) for BFS traversal = O(n)
# Space Complexity: O(n) for the graph + O(n) for BFS queue = O(n)

        