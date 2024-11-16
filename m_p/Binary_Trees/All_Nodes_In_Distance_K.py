from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Step 1: Create a parent map to allow upward traversal
        parent_map = {}
        
        # Helper function to populate the parent map
        def build_parent_map(node, parent=None):
            if node:
                parent_map[node] = parent
                build_parent_map(node.left, node)
                build_parent_map(node.right, node)
        
        # Build the parent map starting from the root
        build_parent_map(root)
        
        # Step 2: Perform BFS starting from the target node
        queue = deque([(target, 0)])  # (current node, distance from target)
        visited = set()  # To track visited nodes
        visited.add(target)
        
        result = []  # To store nodes at distance k
        
        while queue:
            node, distance = queue.popleft()
            
            # If the current distance is equal to k, collect the node's value
            if distance == k:
                result.append(node.val)
            
            # If the distance is less than k, continue exploring neighbors
            if distance < k:
                neighbors = [node.left, node.right, parent_map[node]]
                for neighbor in neighbors:
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))
        
        return result
