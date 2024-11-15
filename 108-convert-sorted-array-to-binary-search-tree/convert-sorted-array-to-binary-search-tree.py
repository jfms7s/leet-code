# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def buildTree(nums: List[int],left,right):

            if left == right:
                return None

            pivot = (left+right) // 2

            return TreeNode(
                val=nums[pivot],
                left=buildTree(nums,left,pivot),
                right=buildTree(nums,pivot+1,right)
            )


        return buildTree(nums,0,len(nums))
        