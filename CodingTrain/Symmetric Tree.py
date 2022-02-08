class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bt(a,b):
            if not a and not b: return True
            if not a or not b: return False
            if a.val != b.val: return False
            return bt(a.left, b.right) and bt(a.right, b.left)
        if not root: return True
        return bt(root.left, root.right)