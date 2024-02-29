# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def mode(root):
            if not root:
                return []
            look_up[root.val] += 1
            mode(root.left)
            mode(root.right)
        look_up = defaultdict(int)
        mode(root)
        theMode = max(look_up.values())
        ans = []
        for val, num in look_up.items():
            if num == theMode:
                ans.append(val)
        return ans

        
        
    
