# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        size = len(nums)
        pivot = size // 2

        return TreeNode(
            val=nums[pivot],
            left=self.sortedArrayToBST(nums[0:pivot]),
            right=self.sortedArrayToBST(nums[pivot+1:size])
        )
        