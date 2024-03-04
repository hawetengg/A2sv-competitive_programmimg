# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBst(left, right):
            if left == right:
                return TreeNode(nums[left])
            if left > right:
                return
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            left_s = makeBst(left, mid - 1)
            right_s = makeBst(mid + 1 , right)
            root.left = left_s
            root.right = right_s
            return root
        return makeBst(0, len(nums) - 1)
        