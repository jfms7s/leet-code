# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        prev = start = current = ListNode(val=None,next=head)

        while(current:=current.next):

            if current.val == val:
                prev.next = current.next
            else:
                prev = current

        return start.next
