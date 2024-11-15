# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_balance(root: Optional[TreeNode]):

            if not root:
                return 0
            
            left = check_balance(root.left)
            right = check_balance(root.right)
            if left == -1 or right == -1:
                return -1

            if abs(left - right) > 1:
                return -1
            
            return max(left,right) +1

        return check_balance(root) >=0
