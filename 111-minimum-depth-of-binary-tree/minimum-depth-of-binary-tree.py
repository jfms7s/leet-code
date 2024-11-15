
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        nodes = [root]
        level = 0

        while nodes:
            level += 1
            new_nodes = []
            for node in nodes:

                if not(node.left or node.right):
                    return level

                node.left and new_nodes.append(node.left)
                node.right and new_nodes.append(node.right)
            nodes = new_nodes
