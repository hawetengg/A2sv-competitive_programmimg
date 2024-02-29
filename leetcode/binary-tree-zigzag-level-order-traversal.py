# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        arr = []

        def traversal(node, y):
            if not node:
                return

            if len(arr) == y:
                arr.append([])

            arr[y].append(node.val)
            traversal(node.left, y + 1)
            traversal(node.right, y + 1)

        traversal(root, 0)

        for i in range(len(arr)):
            if i % 2 != 0:
                arr[i] = arr[i][::-1]

        return arr
        
            
        
        
        