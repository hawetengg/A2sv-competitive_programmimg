# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def helper(node):
            if node is None:
                return
                
            helper(node.left)

            self.count += 1
            if self.count == k:
                self.output = node.val
                return

            helper(node.right)
            

        self.count = 0
        self.output = 0

        helper(root)

        return self.output

            

    