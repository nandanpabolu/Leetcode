class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        newNode = Node(insertVal)
        
        # Case 1: If the list is empty, create a new circular list
        if not head:
            newNode.next = newNode
            return newNode
        
        # Case 2: If the list has only one node
        if head.next == head:
            head.next = newNode
            newNode.next = head
            return head
        
        # Case 3: Traverse and find the right place to insert
        prev, curr = head, head.next
        while True:
            # Case 3.1: Insert in the middle of two nodes in sorted order
            if prev.val <= insertVal <= curr.val:
                break
            
            # Case 3.2: Insert at the boundary where the list wraps around
            if prev.val > curr.val:
                # Insert if insertVal is either the smallest or the largest value
                if insertVal >= prev.val or insertVal <= curr.val:
                    break
            
            # Move to the next node
            prev, curr = curr, curr.next
            
            # If we complete a full cycle around the list, just insert after prev
            if prev == head:
                break
        
        # Insert the new node between prev and curr
        prev.next = newNode
        newNode.next = curr
        
        return head
