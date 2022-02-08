class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root, sub):
            if root == None and sub == None: return True
            if root == None or sub == None: return False
            return root.val == sub.val and check(root.left, sub.left) and check(root.right, sub.right)
        
        return check(root, subRoot) or (root.left and self.isSubtree(root.left, subRoot)) or (root.right and self.isSubtree(root.right, subRoot))
