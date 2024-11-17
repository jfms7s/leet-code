# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = ListNode(val=None,next=head)
        previous = None
        next_node = current.next
        while current := next_node:
            next_node = current.next
            current.next = previous
            previous = current

        return previous