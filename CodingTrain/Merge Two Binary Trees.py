class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs (n1, n2):
            if not n1 or not n2: return
            if n1 and n2: n1.val = n1.val + n2.val
            
            if not n1.left and n2.left:
                n1.left = n2.left
                n2.left = None
            if not n1.right and n2.right:
                n1.right = n2.right
                n2.right = None
                
            dfs(n1.left, n2.left)
            dfs(n1.right, n2.right)
            
        if root1 and not root2: return root1
        if not root1 and root2: return root2
        
        dfs(root1,root2)
        return root1