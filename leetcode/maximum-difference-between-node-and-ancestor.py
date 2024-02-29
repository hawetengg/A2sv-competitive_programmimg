# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, value=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def checker(value, minValue, maxValue):

            if not value:
                return 0

            self.ans = max(self.ans, abs(value.val - minValue), abs(value.val - maxValue))

            maxValue = max(value.val, maxValue)
            minValue = min(value.val, minValue)
            checker(value.left, minValue, maxValue)
            checker(value.right, minValue, maxValue)
            
        self.ans = 0

        checker(root, root.val, root.val)

        return self.ans




        
        
        