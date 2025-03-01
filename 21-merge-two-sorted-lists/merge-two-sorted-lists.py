# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        start_node = current_node = ListNode(val=200)
        while (list1 and list2):

            if list1.val >= list2.val:
                current_node.next = list2
                list2 = list2.next
            else:
                current_node.next = list1
                list1 = list1.next
            current_node = current_node.next

        if(list1):
            current_node.next = list1
        else: 
            current_node.next = list2
        
        return start_node.next