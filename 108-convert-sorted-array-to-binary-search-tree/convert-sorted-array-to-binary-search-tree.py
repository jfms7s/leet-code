# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int],left=None,right=None) -> Optional[TreeNode]:
        if left is None:
            left = 0
        
        if right is None:
            right = len(nums)

        if left == right:
            return None

        pivot = (left+right) // 2

        return TreeNode(
            val=nums[pivot],
            left=self.sortedArrayToBST(nums,left,pivot),
            right=self.sortedArrayToBST(nums,pivot+1,right)
        )
        