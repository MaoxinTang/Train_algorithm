class Solution:
    def __init__(self):
       pass
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        else:
            return 0