# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        first = dummy
        second = dummy

        for _ in range(n+1):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        second.next = second.next.next

        return dummy.next

#Time Complexity is O(L) where L is the length of the list
#Space Complexity is O(1) since no other variables used other than fixed ones