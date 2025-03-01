# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ## alternative implementation, tuple one side and reverse the other
    def symetric(self,p,q):
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False

        return self.symetric(p.left,q.right) and self.symetric(p.right,q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.symetric(root.left,root.right)
