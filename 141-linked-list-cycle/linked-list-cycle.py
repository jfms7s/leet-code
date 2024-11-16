# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head and head.next is None:
            return False
            
        fast = slow = ListNode (val = None, next = head)
        
        while (fast := fast.next) and (fast := fast.next) and (slow := slow.next):
            if fast == slow:
                return True
        
        return False