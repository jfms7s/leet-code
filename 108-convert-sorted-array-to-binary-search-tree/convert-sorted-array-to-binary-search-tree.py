# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTree(self,nums: List[int],left,right):

        if left == right:
            return None

        pivot = (left+right) // 2

        return TreeNode(
            val=nums[pivot],
            left=self.buildTree(nums,left,pivot),
            right=self.buildTree(nums,pivot+1,right)
        )


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.buildTree(nums,0,len(nums))
        