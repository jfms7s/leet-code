# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if head is None:
            return None

        size = 0
        tail = None
        current = head
        
        while current:
            size += 1
            tail = current
            current = current.next

        
        tail.next = head
        size = size - (k % size)
        current = tail
        
        while size>0:
            current = current.next
            current 
            size -= 1

        head = current.next
        current.next = None

        return head

