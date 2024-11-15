
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def minDepth(root: Optional[TreeNode], depth=0) -> int:
    l = root.left and minDepth(root.left,depth+1)
    r = root.right and minDepth(root.right,depth+1)

    if not (l or r):
        return depth

    if l and r:
        return min(l,r)

    return r or l


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        return minDepth(root,1 )