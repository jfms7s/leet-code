# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start_pointer = ListNode(val=None, next=head)
        
        current_node = start_pointer
        prev_node = start_pointer
        while current_node := current_node.next:
            
            if prev_node.val == current_node.val:
                prev_node.next = current_node.next
            else:
                prev_node.next = current_node
                prev_node = current_node

        return start_pointer.next