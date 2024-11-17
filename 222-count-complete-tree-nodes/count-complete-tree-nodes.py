# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        r_count = 1
        next_node = root
        while next_node := next_node.left: r_count += 1

        l_count = 1
        next_node = root
        while next_node := next_node.right: l_count += 1

        print(f"{root.val=} {r_count=} {l_count=}")
        if r_count == l_count:
            print(f"balance {root.val=} {2 ** l_count=}")
            return (2 ** l_count)-1

        result = 1 + self.countNodes(root.left) + self.countNodes(root.right)
        print(f"unbalance {root.val=} {result=}")
        return result